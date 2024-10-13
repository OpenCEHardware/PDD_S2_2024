import subprocess
import os
import argparse
from pathlib import Path

import yaml_reader as yr
import template_generator as tg
import makefile_generator as mg
import Utils as U


# ================================================================================================================
g_yaml_path = ''
g_run_make = False
g_compile = False
g_src_dir = os.getcwd()

COMMAND = "make"

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


# def has_compilated_files(metadata: yr.Metadata) -> bool:
    
#     path = Path(metadata.output_dir) + COMPILED_FILES_DIR
#     print(f"PATH: {path}")
#     return Path(path).is_dir()


def general_exec(command=COMMAND, dir=None, show_stdout=True, show_stderr=True, show_exit_code=True):
    if show_stdout:
        U.print_dash_line('-')
        if(U.g_os_name == U.OS.WINDOWS.value):
            print("Accessing WSL")
        else:
            print("Accessing Terminal")

    try:
        objetive_dir = os.path.join(g_src_dir, dir)

        if dir:
            if show_stdout:
                print(f"Moving to dir: {objetive_dir}")
            os.chdir(objetive_dir)

        if(U.g_os_name == U.OS.WINDOWS.value):
            exec_powershell_wsl(command, show_stdout, show_stderr, show_exit_code)
        else:
            exec_terminal(command, show_stdout, show_stderr, show_exit_code)

        os.chdir(g_src_dir)
    except subprocess.CalledProcessError as e:
        # print(f"general_excec/Error: {e}")
        pass

def show_command_info(result, command, show_stdout, show_stderr, show_exit_code):
    U.print_dash_line('-')
    if(U.g_os_name == U.OS.WINDOWS.value):
        print("WSL command executed:")
    else:
        print("Terminal command executed:")        
    print(command)
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


def exec_powershell_wsl(wsl_command, show_stdout, show_stderr, show_exit_code):
    powershell_command = f'wsl -e bash -ic "{wsl_command}"'
    result = subprocess.run(["powershell", "-Command", powershell_command], capture_output=True, text=True)
    show_command_info(result, powershell_command, show_stdout, show_stderr, show_exit_code)


def exec_terminal(command, show_stdout, show_stderr, show_exit_code):
    result = subprocess.run(command, check=True, text=True, capture_output=True)
    show_command_info(result, command, show_stdout, show_stderr, show_exit_code)


def cmd_parser():
    global g_yaml_path, g_run_make, g_compile
    parser = argparse.ArgumentParser(description="Tool entrypoint.")

    parser.add_argument(
        "yaml_filepath", 
        type=str,
        help="Filepath of the yaml config file."
    )
    parser.add_argument(
        "-r",
        action="store_true",
        help="Run make without overwriting template."
    )
    parser.add_argument(
        "-c",
        action="store_true",
        help="Run make without overwriting template and makefile."
    )
    parser.add_argument(
        "--verbose", 
        action="store_true", 
        help="Show detailed info."
    )

    args = parser.parse_args()

    if args.verbose:
        print("Detailed mode activate.")

    # set globals values
    g_yaml_path = args.yaml_filepath
    g_run_make = args.r
    g_compile = args.c

if __name__ == "__main__":
    U.recognize_os()
    cmd_parser()

    if(g_compile and g_run_make):
        raise RuntimeError("Use just 1 flag between -r and -c")
    else:
        metadata = yr.read_yaml(g_yaml_path) # <- gens output folder

        U.g_TEST_PATH = metadata.output_dir
        U.g_SIM_BUILD_PATH = os.path.join(metadata.output_dir, U.g_SIM_BUILD_PATH)
        # print(f"U.g_TEST_PATH: {U.g_TEST_PATH}")
        # print(f"U.g_SIM_BUILD_PATH: {U.g_SIM_BUILD_PATH}")

        U.covert_template_paths()

        is_sim_build_a_dir = Path(U.g_SIM_BUILD_PATH).is_dir()
        is_sim_build_empty = True
        if(is_sim_build_a_dir):
            is_sim_build_empty = U.is_directory_empty(U.g_SIM_BUILD_PATH)

        if(not g_run_make):
            tg.gen_template(metadata, template_option=metadata.template_type)
        else:
            U.print_dash_line()
            print("Using current template")

        is_output_dir_empty = U.is_directory_empty(U.g_TEST_PATH)
        if not is_output_dir_empty:
            mg.gen_makefile(metadata)


        if(U.g_os_name == U.OS.WINDOWS.value):
            has_wsl = check_wsl_installed()
            if(not has_wsl):
                raise RuntimeError("Missing WSL")

        U.print_dash_line()
        if(not is_sim_build_a_dir and g_compile):
            print("Compiling")
            general_exec(dir=metadata.output_dir, show_stderr=False, show_exit_code=False)
        elif(not is_sim_build_a_dir and not g_compile and is_output_dir_empty):
            print("There is no template")
        elif(not is_sim_build_a_dir and not g_compile and not is_output_dir_empty):
            print("Compiling and running")
            print(metadata.output_dir)
            general_exec(dir=metadata.output_dir, show_stdout=False, show_stderr=False, show_exit_code=False)
            general_exec(dir=metadata.output_dir)
        elif(is_sim_build_a_dir and is_sim_build_empty and g_compile):
            print("Retrying compilation")
            general_exec(dir=metadata.output_dir)
        elif(is_sim_build_a_dir and not is_sim_build_empty and g_compile):
            print("Done")
        elif(is_sim_build_a_dir and not is_sim_build_empty and not g_compile):
            print("Running")
            general_exec(dir=metadata.output_dir)
        U.print_dash_line()
        print("Done")

# # Obtener el PATH actual y agregar el nuevo directorio
# current_path = os.environ['PATH']
# new_path_env = f"{U.g_QUESTA_BIN_PATH}:{current_path}"

# bash_command = f'PATH="{new_path_env}" command -v vsim'
# result = subprocess.run(["bash", "-c", bash_command], capture_output=True, text=True)
# show_command_info(result, bash_command)

# bash_command = "source /root/.bashrc && printenv PATH"
# result = subprocess.run(["wsl", "bash", "--noprofile", "-c", "printenv PATH"], capture_output=True, text=True)
# show_command_info(result, bash_command)


# bash_command = "source /root/.bashrc && printenv PATH"
# # bash_command = "source ~/.bashrc && echo $PATH"

# result = subprocess.run(["wsl", "bash", "-l", "-c", bash_command], capture_output=True, text=True)
# show_command_info(result, bash_command)

# bash_command = "echo $PATH"
# bash_command = "printenv PATH"
# result = subprocess.run(["wsl", "bash", "-l", "-c", "printenv PATH"], capture_output=True, text=True)
# show_command_info(result, bash_command)

# bash_command = "whereis vsim"
# result = subprocess.run(["wsl", "bash", "-l", "-c", bash_command], capture_output=True, text=True)
# show_command_info(result, bash_command)
