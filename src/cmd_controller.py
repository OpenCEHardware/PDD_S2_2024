import subprocess
import os
import argparse
from pathlib import Path

import yaml_reader as yr
import template_generator as tg
import makefile_generator as mg
import Utils as U


# ================================================================================================================
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


def exec_WSL(comand=COMMAND, dir=None, show=True):
    # print(f"dir: {dir}")
    actual_dir = os.getcwd()
    # print(f"actual_dir: {actual_dir}")
    # objetive_dir = os.path.join(actual_dir, dir)
    # print(f"objetive_dir: {objetive_dir}")

    if show:
        U.print_dash_line('-')
        print("Accessign WSL")
    try:
        objetive_dir = os.path.join(actual_dir, dir)

        if dir:
            if show:
                print(f"Moving to dir: {objetive_dir}")
            os.chdir(objetive_dir)

        if show:
            print(f"Running: {comand}")
        result = subprocess.run(['wsl', comand], shell=True, capture_output=True, text=True)

        if show:
            U.print_dash_line('-')
            print("WSL output:")
            U.print_dash_line('-')
            print(result.stdout)

        os.chdir(actual_dir)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


def cmd_parser():
    global g_yaml_path
    parser = argparse.ArgumentParser(description="Tool entrypoint.")

    parser.add_argument(
        "yaml_filepath", 
        type=str,
        help="Filepath of the yaml config file."
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


if __name__ == "__main__":
    U.recognize_os()
    cmd_parser()
    metadata = yr.read_yaml(g_yaml_path)
    tg.gen_template(metadata, template_option=1)
    mg.gen_makefile(metadata)

    if(U.g_os_name == U.OS.WINDOWS.value):
        has_wsl = check_wsl_installed()
        if(has_wsl):
            exec_WSL(dir=metadata.output_dir, show=False)
            exec_WSL(dir=metadata.output_dir)
    else:
        print("UBUNTU TO DO")



        # if(not has_compilated_files(metadata)):
        #     print("HASNT")
        #     exec_WSL(dir=metadata.output_dir, show=False)
        # exec_WSL(dir=metadata.output_dir)
