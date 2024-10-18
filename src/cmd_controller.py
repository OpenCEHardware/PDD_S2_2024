#=======================================================================================================
# Imports
#=======================================================================================================
import subprocess
import os
import sys
import shutil
import argparse
from pathlib import Path
import time

import yaml_reader as yr
import template_generator as tg
import makefile_generator as mg
import quartus_synth_manager as qsm
import Utils as U

# https://docs.cocotb.org/en/stable/building.html#envvar-COCOTB_ENABLE_PROFILING
#=======================================================================================================
# Globals
#=======================================================================================================
# paths
g_yaml_path = ''
g_src_dir = os.getcwd()
TXT_TO_KNOW_PREVIOUS_SIMULATOR = "sim.txt"

# flags
g_reset_template = False
g_execute = False

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
#=======================================================================================================
# Defs
#=======================================================================================================
def check_wsl_installed():
    """
    Checks if Windows Subsystem for Linux (WSL) is installed and enabled on the system.

    This function attempts to run the `wsl --list` command to check for installed WSL distributions.
    If WSL is not enabled or an error occurs during the command execution, it prints an error message.
    It returns a boolean indicating whether WSL is installed and enabled.

    Raises:
        subprocess.CalledProcessError: If there is an error executing the `wsl` command.
    """
    if(U.g_os_name == U.OS.WINDOWS.value):
        has_WSL = False
        try:
            result = subprocess.run(["wsl", "--list"], capture_output=True, text=True, check=True)

            if NO_WSL_MSG_ERR_STR in result.stderr:
                print("WSL is not enabled on your system.")
            else:
                has_WSL = True

        except subprocess.CalledProcessError as e:
            print(f"Error verifiying WSL: {e}")

        if(not has_WSL):
            raise RuntimeError("Missing WSL")


def general_exec \
    (
        command_receiver=U.COMMAND_RECEIVER.WSL.value,
        command=MAKE_COMMAND,
        dir=None,
        show_stdout=True,
        show_stderr=True,
        show_exit_code=True
    ):
    """
    Executes a command in the specified environment (WSL or Terminal).

    This function allows the execution of a command either in Windows Subsystem for Linux (WSL) or a terminal,
    depending on the operating system. It supports handling output display options such as stdout, stderr, 
    and exit code. The command is executed from a specific directory if provided, and it returns to the 
    original directory after execution.

    Args:
        command_receiver (str): Specifies the environment to run the command, either PowerShell, WSL or Terminal.
        command (str): The command to be executed.
        dir (str, optional): The directory to switch to before executing the command. Defaults to None.
        show_stdout (bool, optional): Whether to display standard output. Defaults to True.
        show_stderr (bool, optional): Whether to display standard error output. Defaults to True.
        show_exit_code (bool, optional): Whether to display the exit code of the command. Defaults to True.

    Raises:
        subprocess.CalledProcessError: If the command execution fails or encounters an error.

    Returns:
        None: The function does not return any value but may raise exceptions on errors.
    """
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
    """
    Displays the result information of a command execution.

    Args:
        result: The result object of the executed command (should contain stdout, stderr, returncode).
        command (str): The command that was executed.
        show_stdout (bool): Whether to display the standard output.
        show_stderr (bool): Whether to display the standard error output.
        show_exit_code (bool): Whether to display the exit code of the command.
    """
    U.print_dash_line('-')
    
    # Display the command being executed
    if show_stdout or show_stderr or show_exit_code:
        print(f"Running command: {command}")
        U.print_dash_line('-')

    # Show stdout
    if show_stdout:
        print(f"stdout (output):")
        print(result.stdout if result.stdout else "No stdout")
        U.print_dash_line('-')

    # Show stderr
    if show_stderr:
        print(f"stderr (errors):")
        print(result.stderr if result.stderr else "No stderr")
        U.print_dash_line('-')

    # Show exit code and status
    if show_exit_code:
        print(f"Return code: {result.returncode}")
        U.print_dash_line('-')

        # Check command success
        if result.returncode != 0:
            print("The command failed.")
        else:
            print("The command succeeded.")


def exec_powershell(command):
    """
    Executes a PowerShell command using subprocess.

    Args:
        command (str): The PowerShell command to execute.
        timeout (int, optional): Maximum time to wait for command execution. Defaults to None.

    Returns:
        subprocess.CompletedProcess: Result of the command execution, including stdout, stderr, and returncode.
    """
    return subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)


def convert_command_to_PS_WSL(command):
    """
    Converts a command intended for a Unix-like shell into a format that can be run via PowerShell using WSL (Windows Subsystem for Linux).

    This function wraps the given command string in a format that runs the command in WSL (Windows Subsystem for Linux) through PowerShell. It uses `wsl -e bash -ic` to invoke the bash shell in WSL and pass the command for execution.

    Flags used:
        - `-e`: Specifies the executable that WSL should run (in this case, `bash`). Without this, WSL runs the default shell. The `-e` flag allows you to specify another shell or program to execute.
        - `-i`: Starts an interactive shell session. This ensures that user-specific startup files are executed, and the session behaves like a regular interactive terminal.
        - `-c`: Executes the command provided as a string argument to the shell. It runs the command and then exits.
        - `-ic`: Combines `-i` and `-c` to first start an interactive shell (`-i`), then execute the command passed as an argument (`-c`). This allows you to run commands in an interactive environment and execute them immediately.

    Args:
        command (str): The command to be executed in the WSL bash environment.

    Returns:
        str: A formatted string that runs the given command in WSL via PowerShell.
    
    Example:
        >>> convert_command_to_PS_WSL("ls")
        'wsl -e bash -ic "ls"'
    """
    return f'wsl -e bash -ic "{command}"'


def exec_terminal(command):
    return subprocess.run(command, check=True, text=True, capture_output=True)


def cmd_parser():
    global g_yaml_path, g_reset_template, g_execute
    parser = argparse.ArgumentParser(description="Tool entrypoint.")

    parser.add_argument \
    (
        "yaml_filepath", 
        type=str,
        help="Filepath of the yaml config file."
    )

    parser.add_argument \
    (
        "-e",
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
    g_execute = args.e


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


def gen_template(metadata: yr.Metadata):
    get_template_status()
    if(g_exists_template):
        if(g_reset_template):
            tg.gen_template(metadata)
        else:
            print("Using current template")
    else:
        tg.gen_template(metadata)


def gen_makefile(metadata: yr.Metadata):
    get_makefile_status()
    mg.gen_makefile(metadata)


def handle_quartus(metadata: yr.Metadata):
    global g_is_quartus_p_a_dir, g_is_quartus_p_empty

    # Check dir and dir emptyness
    if(metadata.quartus_project_path):
        g_is_quartus_p_a_dir = Path(metadata.quartus_project_path).is_dir()

    if(g_is_quartus_p_a_dir):
        g_is_quartus_p_empty = U.is_directory_empty(metadata.quartus_project_path)

    if(not g_is_quartus_p_a_dir or g_is_quartus_p_empty):
        print(f"Warning: There is no Quartus project")

    else:
        print("Checking Quartus")
        qsm.handle_quartus_synthesis(metadata)


def execute():
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
#=======================================================================================================
# Entrypoint
#=======================================================================================================
if __name__ == "__main__":    
    U.recognize_os()
    check_wsl_installed()
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

    # Preparation
    if not g_execute:
        # Template
        U.print_dash_line()
        gen_template(metadata)

        # Makefile
        U.print_dash_line()
        gen_makefile(metadata)
    
        # Quartus project
        U.print_dash_line()
        handle_quartus(metadata)

        U.print_dash_line()
        print(f"Done.")
        U.print_dash_line()

    # Execute
    if g_execute:
        # Get duration
        start_time = time.time()

        U.print_dash_line()
        execute()

        # Get duration
        end_time = time.time()
        duration = end_time - start_time

        U.print_dash_line()
        print(f"Done. Duration: {duration:.2f}s")
        U.print_dash_line()
