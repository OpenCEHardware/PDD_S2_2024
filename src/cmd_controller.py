#=======================================================================================================
# Imports
#=======================================================================================================
import subprocess
import os
import sys
import shutil
import argparse
from pathlib import Path

import yaml_reader as yr
import template_generator as tg
import makefile_generator as mg
import Utils as U

# https://docs.cocotb.org/en/stable/building.html#envvar-COCOTB_ENABLE_PROFILING
# ================================================================================================================
# paths
g_yaml_path = ''
g_src_dir = os.getcwd()
TXT_TO_KNOW_PREVIOUS_SIMULATOR = "sim.txt"

# flags
g_reset_template = False
g_compile = False

# qsf default values
QUARTUS_PROJECT_NAME = "project"
g_family = "Cyclone V"
g_device = "AUTO"
g_top_level_entity = "project"

# commands
MAKE_COMMAND = "make"
CREATE_QUARTUS_PROJECT_COMMAND = f"quartus_sh --prepare {QUARTUS_PROJECT_NAME}.qpf" # PSC
COMPILE_COMPILE_PROJECT = f"quartus_sh --flow compile {QUARTUS_PROJECT_NAME}"

# Execution Control variables
g_is_output_a_dir = False
g_is_output_empty = True
g_exists_template = False
g_exists_makefile = True
g_is_sim_build_a_dir = False
g_is_sim_build_empty = True
g_is_quartus_p_a_dir = False
g_is_quartus_p_empty = True
g_simulator = ""

# Error msgs
NO_WSL_MSG_ERR_STR = "Windows Subsystem for Linux has not been enabled"
# ================================================================================================================
### Checks
## WSL
def check_wsl_installed():
    """
    Checks if Windows Subsystem for Linux (WSL) is installed and enabled on the system.

    This function attempts to run the `wsl --list` command to check for installed WSL distributions.
    If WSL is not enabled or an error occurs during the command execution, it prints an error message.
    It returns a boolean indicating whether WSL is installed and enabled.

    Returns:
        bool: True if WSL is installed and enabled, False otherwise.

    Raises:
        subprocess.CalledProcessError: If there is an error executing the `wsl` command.
    """

    has_WSL = False
    try:
        result = subprocess.run(["wsl", "--list"], capture_output=True, text=True, check=True)

        if NO_WSL_MSG_ERR_STR in result.stderr:
            print("WSL is not enabled on your system.")
        else:
            # print("WSL está instalado y habilitado.")
            # print("Distribuciones instaladas:")
            # print(result.stdout)
            has_WSL = True
    except subprocess.CalledProcessError as e:
        print(f"Error verifiying WSL: {e}")
    return has_WSL


def check_sv_file(file_path):
    directory = os.path.dirname(file_path)
    
    # Check that the directory exists
    if not os.path.isdir(directory):
        raise argparse.ArgumentTypeError(f"The directory '{directory}' does not exist.")

    # Check that the file exists
    if not os.path.isfile(file_path):
        raise argparse.ArgumentTypeError(f"The file '{file_path}' does not exist.")

    # Check that the file has a .sv extension
    if not file_path.endswith('.sv'):
        raise argparse.ArgumentTypeError(f"The file '{file_path}' does not have a .sv extension.")
    
    return file_path


def general_exec \
    (
        command_receiver=U.COMMAND_RECEIVER.WSL.value,
        command=MAKE_COMMAND,
        dir=None,
        show_stdout=True,
        show_stderr=True,
        show_exit_code=True
    ):

    if show_stdout:
        U.print_dash_line('-')
        if(U.g_os_name == U.OS.WINDOWS.value):
            if(command_receiver == U.COMMAND_RECEIVER.WSL.value):
                print("Accessing WSL")
        else:
            print("Accessing Terminal")

    try:
        objetive_dir = os.path.join(g_src_dir, dir)

        if dir:
            if show_stdout:
                print(f"Moving to dir: {objetive_dir}")
            os.chdir(objetive_dir)

        result = None
        if(U.g_os_name == U.OS.WINDOWS.value):
            if(command_receiver == U.COMMAND_RECEIVER.WSL.value):
                command = convert_command_to_PS_WSL(command)
            result = exec_powershell(command)
        else: # Ubuntu
            result = exec_terminal(command)

        show_command_info(result, command, show_stdout, show_stderr, show_exit_code)

        os.chdir(g_src_dir)
    except subprocess.CalledProcessError as e:
        # print(f"general_excec/Error: {e}")
        pass


def show_command_info(result, command, show_stdout, show_stderr, show_exit_code):
    U.print_dash_line('-')

    if(show_stdout or show_stderr or show_exit_code):
        print(f"Executing the command: {command}")
        U.print_dash_line('-')

        if show_stdout:
            if(U.g_os_name == U.OS.WINDOWS.value):
                print("WSL stdout (output):")
            else:
                print("Terminal stdout (output):")
            print(result.stdout if result.stdout else "No stdout")
            U.print_dash_line('-')

        if show_stderr:
            if(U.g_os_name == U.OS.WINDOWS.value):
                print("WSL stderr (errors):")
            else:
                print("Terminal stderr (errors):")
            print(result.stderr if result.stderr else "No stderr")
            U.print_dash_line('-')

        if show_exit_code:
            print(f"Return code: {result.returncode}")
            U.print_dash_line('-')

            if result.returncode != 0:
                print("The command failed.")
            else:
                print("The command succeeded.")

def exec_powershell(command):
    return subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)

def convert_command_to_PS_WSL(command):
    return f'wsl -e bash -ic "{command}"'

def exec_terminal(command):
    return subprocess.run(command, check=True, text=True, capture_output=True)


def modify_qsf \
    (
        metadata: yr.Metadata,
        family = 'Cyclone V',
        device = 'AUTO',
        top_level_entity = 'project',
        # original_quartus_version = '20.1.0',
        # project_creation_time_date = '02:48:38  OCTOBER 17, 2024',
        # last_quartus_version = '20.1.0 Lite Edition'
    ):

    qsf_filepath = os.path.join(U.g_quartus_dir, f"{QUARTUS_PROJECT_NAME}.qsf")

    with open(qsf_filepath, 'r') as file:
        lines = file.readlines()

    assignments_to_change = \
    {
        "FAMILY": f'"{family}"'
        ,"DEVICE": device
        ,"TOP_LEVEL_ENTITY": top_level_entity
        # ,"ORIGINAL_QUARTUS_VERSION" : original_quartus_version
        # ,"PROJECT_CREATION_TIME_DATE" : project_creation_time_date
        # ,"LAST_QUARTUS_VERSION" : last_quartus_version
    }

    for key, value in assignments_to_change.items():
        for i in range(len(lines)):
            if key in lines[i]:
                lines[i] = f'set_global_assignment -name {key} {value}\n'

    lines.append("\n\n\n")

    sv_files = U.find_sv_files(metadata.get_comined_path_list())
    for sv in sv_files:
        lines.append(f'set_global_assignment -name VERILOG_FILE {sv}\n')

    with open(qsf_filepath, 'w') as file:
        file.writelines(lines)

# set_global_assignment -name FAMILY "Cyclone V"
# set_global_assignment -name DEVICE AUTO
# set_global_assignment -name TOP_LEVEL_ENTITY project
# set_global_assignment -name ORIGINAL_QUARTUS_VERSION 20.1.0
# set_global_assignment -name PROJECT_CREATION_TIME_DATE "03:18:32  OCTOBER 17, 2024"
# set_global_assignment -name LAST_QUARTUS_VERSION "20.1.0 Lite Edition"


def cmd_parser():
    global g_yaml_path, g_reset_template, g_compile
    parser = argparse.ArgumentParser(description="Tool entrypoint.")

    parser.add_argument \
    (
        "yaml_filepath", 
        type=str,
        help="Filepath of the yaml config file."
    )

    parser.add_argument \
    (
        "-c",
        action="store_true",
        help="Run make without overwriting template and makefile."
    )

    parser.add_argument \
    (
        "-r",
        action="store_true",
        help="Run make without overwriting template."
    )

    parser.add_argument \
    (
        "--verbose", 
        action="store_true", 
        help="Show detailed info."
    )

    args = parser.parse_args()

    if args.verbose:
        print("Detailed mode activate.")

    # set globals values
    g_yaml_path = args.yaml_filepath
    g_reset_template = args.r
    g_compile = args.c

    try:
        if(g_compile and g_reset_template):
            raise RuntimeError("Use just 1 flag between -c and -r")
    except RuntimeError as e:
        print(e)
        sys.exit()


def get_output_dir_status():
    global g_is_output_a_dir, g_is_output_empty
    g_is_output_a_dir = Path(U.g_output_dir).is_dir()
    if(g_is_output_a_dir):
        g_is_output_empty = U.is_directory_empty(U.g_output_dir)


def get_sim_build_dir_status():
    global g_is_sim_build_a_dir, g_is_sim_build_empty
    g_is_sim_build_a_dir = Path(U.g_sim_build_dir).is_dir()
    if(g_is_sim_build_a_dir):
        g_is_sim_build_empty = U.is_directory_empty(U.g_sim_build_dir)

def get_quartus_p_dir_status():
    global g_is_quartus_p_a_dir, g_is_quartus_p_empty
    g_is_quartus_p_a_dir = Path(U.g_quartus_dir).is_dir()
    if(g_is_quartus_p_a_dir):
        g_is_quartus_p_empty = U.is_directory_empty(U.g_quartus_dir)


def get_template_status():
    global g_exists_template 
    g_exists_template = U.file_exists(file_name=metadata.template_name+".py", dir=U.g_output_dir)


def get_makefile_status():
    global g_exists_makefile
    g_exists_makefile = U.file_exists("Makefile", dir=U.g_output_dir)


def get_simulator_status(metadata: yr.Metadata):
    global g_simulator
    g_simulator = metadata.simulator.lower()
    if(g_simulator == U.SIM.VERILATOR.value.lower()):
        g_simulator = U.SIM.VERILATOR.value
    elif(g_simulator == U.SIM.QUESTA.value.lower()):
        g_simulator = U.SIM.QUESTA.value        


def check_simulator_change(metadata: yr.Metadata):
    previous_simulator = U.read_from_txt(TXT_TO_KNOW_PREVIOUS_SIMULATOR)
    U.write_to_txt(TXT_TO_KNOW_PREVIOUS_SIMULATOR, g_simulator)
    if(previous_simulator != g_simulator):
        U.clear_directory_except(dir=U.g_output_dir, filename_to_keep=f"{metadata.template_name}.py")


def check_errors():
    # Handling errors
    get_output_dir_status()
    if(not g_is_output_a_dir):
        print("Error generating output dir")
        sys.exit()

    if(g_is_output_empty):
        print("Error writing data in output dir")
        sys.exit()

    get_template_status()
    if(not g_exists_template):
        print("Error reading template")
        sys.exit()

    get_makefile_status()
    if(not g_exists_makefile):
        print("Error reading Makefile")
        sys.exit()

    get_quartus_p_dir_status()
    if(not g_is_quartus_p_a_dir):
        print("Error generating quartus_p dir")
        sys.exit()


def start():
    # Execute
    if(not g_is_sim_build_a_dir):
        print("Compiling and running")
        if(g_simulator == U.SIM.VERILATOR.value):
            general_exec(dir=metadata.output_dir, show_stdout=False, show_stderr=False, show_exit_code=False)
        general_exec(dir=metadata.output_dir, show_stdout=True, show_stderr=True, show_exit_code=True)

    elif(g_is_sim_build_a_dir and g_is_sim_build_empty):
        print("Retrying compilation")
        general_exec(dir=metadata.output_dir)

    elif(g_is_sim_build_a_dir and not g_is_sim_build_empty):
        print("Running")
        general_exec(dir=metadata.output_dir, show_stdout=True, show_stderr=True, show_exit_code=True)


if __name__ == "__main__":
    # Initialize
    U.recognize_os()
    cmd_parser()

    # Reads YAML
    U.print_dash_line()
    metadata = yr.read_yaml(g_yaml_path) # <- gens output folder

    # Initial control settings
    U.set_output_dirs_from_metadata(metadata)
    U.covert_paths() # Converts default windows paths to linux paths if needed
    get_output_dir_status()
    get_simulator_status(metadata)
    check_simulator_change(metadata) # Clears dir if the sim changes (except the template)
    get_sim_build_dir_status()

    # Template
    U.print_dash_line()
    get_template_status()
    if(g_exists_template):
        if(g_reset_template):
            tg.gen_template(metadata, template_option=metadata.template_type)
        else:
            print("Using current template")
    else:
        tg.gen_template(metadata, template_option=metadata.template_type)

    # Makefile
    U.print_dash_line()
    get_makefile_status()
    mg.gen_makefile(metadata)

    # For Windows checks WSL
    if(U.g_os_name == U.OS.WINDOWS.value):
        has_wsl = check_wsl_installed()
        if(not has_wsl):
            raise RuntimeError("Missing WSL")
    
    # check_errors()

    # Quartus project
    get_quartus_p_dir_status()
    if(not g_is_quartus_p_a_dir or g_is_quartus_p_empty):
        U.print_dash_line()
        if(not g_is_quartus_p_a_dir):
            U.create_dir(folder_path=U.g_quartus_dir)
            print("Creating Quartus dir")
        if(g_is_quartus_p_empty):
            print("Writing .qsf")
            general_exec(command_receiver=U.COMMAND_RECEIVER.POWERSHELL.value,command=CREATE_QUARTUS_PROJECT_COMMAND,show_stdout=False, dir=U.g_quartus_dir)
            modify_qsf(metadata, family=g_family, device=g_device, top_level_entity=g_top_level_entity)

    # Execute
    U.print_dash_line()
    start()

    U.print_dash_line()
    print("Done")
