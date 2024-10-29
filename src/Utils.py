#=======================================================================================================
# Imports
#=======================================================================================================
import shutil
import os
import platform
from enum import Enum
#=======================================================================================================
# Enums
#=======================================================================================================
class OS(Enum):
    """
    Enum for supported operating systems.    
    """
    WINDOWS  = "Windows"
    UBUNTU   = "Ubuntu"

class SIM(Enum):
    """
    Enum for supported simulators.
    """
    VERILATOR = "Verilator"
    QUESTA   = "Questa"

class COMMAND_RECEIVER(Enum):
    """
    Enum for command receivers.
    """
    TERMINAL = "Terminal"
    POWERSHELL = "PowerShell"
    WSL = "WSL"
#=======================================================================================================
# Globals
#=======================================================================================================
g_os_name = ""

# Template dirs
## Paths starts in windows default format
g_TEMPLATE_OPTION_0 = '..\\templates\\arch_simple.txt'
g_TEMPLATE_OPTION_1 = '..\\templates\\arch_structured.txt'
g_TEMPLATE_STRUCTURE_OPTION_0 = '..\\templates\\structure_example_1.txt'

# Output dirs
g_output_dir = ""
g_sim_build_dir = "sim_build"
g_reports_dir = "reports"
#=======================================================================================================
# Defs
#=======================================================================================================
def recognize_os():
    """
    Recognize the operating system and update the global variable g_os_name.
    
    Sets g_os_name to 'Windows' or 'Ubuntu' based on the current platform. Raises a RuntimeError
    if the platform is unsupported.
    """
    global g_os_name

    # Assumes Windows
    g_os_name = OS.WINDOWS.value
    
    current_os = os.name
    if current_os == 'posix':
        if platform.system() == "Linux" and "ubuntu" in platform.version().lower():
            g_os_name = OS.UBUNTU.value
        else:
            raise RuntimeError("Invalid posix platform")
    elif current_os != 'nt':
        raise RuntimeError("Invalid platform, must be Windows or Ubuntu")


def covert_paths():
    """
    Convert global template paths from Windows to Unix format if the OS is Ubuntu.
    
    Updates the paths stored in g_TEMPLATE_OPTION_0, g_TEMPLATE_OPTION_1, g_TEMPLATE_STRUCTURE_OPTION_0,
    g_output_dir, and g_sim_build_dir.
    """
    global g_TEMPLATE_OPTION_0, g_TEMPLATE_OPTION_1, g_TEMPLATE_STRUCTURE_OPTION_0, g_output_dir, g_sim_build_dir
    if(g_os_name == OS.UBUNTU.value):
        g_TEMPLATE_OPTION_0 = windows_to_unix_path(g_TEMPLATE_OPTION_0)
        g_TEMPLATE_OPTION_1 = windows_to_unix_path(g_TEMPLATE_OPTION_1)
        g_TEMPLATE_STRUCTURE_OPTION_0 = windows_to_unix_path(g_TEMPLATE_STRUCTURE_OPTION_0)
        g_output_dir = windows_to_unix_path(g_output_dir)
        g_sim_build_dir = windows_to_unix_path(g_sim_build_dir)

def windows_to_unix_path(windows_path):
    """
    Convert a Windows file path to Unix format.
    
    Args:
        windows_path (str): A file path in Windows format.
    
    Returns:
        str: The path in Unix format.
    """
    return windows_path.replace('\\', '/')


def windows_to_wsl_path(windows_path):
    """
    Convert a Windows file path to WSL (Windows Subsystem for Linux) format.
    
    Args:
        windows_path (str): A file path in Windows format.
    
    Returns:
        str: The path in WSL format.
    """
    wsl_path = windows_to_unix_path(windows_path)
    
    if wsl_path[1:3] == ':/' or wsl_path[1:2] == ':':
        drive_letter = wsl_path[0].lower()
        wsl_path = f'/mnt/{drive_letter}{wsl_path[2:]}'    
    return wsl_path


def is_directory_empty(dir_path):
    """
    Check if the specified directory is empty.
    
    Args:
        dir_path (str): The path to the directory.
    
    Returns:
        bool: True if the directory is empty, False otherwise.
    """
    return not os.listdir(dir_path)


def file_exists(file_name, dir):
    """
    Check if a file exists in the specified directory.
    
    Args:
        file_name (str): The name of the file.
        dir (str): The path to the directory.
    
    Returns:
        bool: True if the file exists, False otherwise.
    """
    file_path = os.path.join(dir, file_name)
    return os.path.isfile(file_path)


def set_output_dirs_from_metadata(metadata):
    """
    Set output directories based on metadata.
    
    Args:
        metadata (object): An object containing output directory information.
    
    Updates the global variables g_output_dir, g_sim_build_dir, and g_reports_dir.
    """
    global g_output_dir, g_sim_build_dir, g_reports_dir
    g_output_dir = metadata.output_dir
    g_sim_build_dir = os.path.join(g_output_dir, g_sim_build_dir)
    g_reports_dir = os.path.join(g_output_dir, g_reports_dir)


def write_to_txt(file_path, content):
    """
    Write content to a text file.
    
    Args:
        file_path (str): The path to the file.
        content (str): The content to write to the file.
    
    Returns:
        str: Success or error message.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        return "File written successfully."
    except Exception as e:
        return f"An error occurred: {e}"


def read_from_txt(file_path) -> str:
    """
    Read content from a text file.
    
    Args:
        file_path (str): The path to the file.
    
    Returns:
        str: The file content or an error message if the file is not found or an error occurs.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"
    

def clear_directory(directory_path):
    """
    Clear the contents of a directory.
    
    Args:
        directory_path (str): The path to the directory.
    
    Returns:
        str: Success message or error message if an error occurs.
    """
    try:
        if os.path.exists(directory_path):
            for item in os.listdir(directory_path):
                item_path = os.path.join(directory_path, item)
                
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.unlink(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
        # else:
        #     return "Directory does not exist."
    except Exception as e:
        return f"An error occurred: {e}"


def clear_directory_except(dir, filename_to_keep):
    """
    Clear a directory except for a specified file.
    
    Args:
        dir (str): The path to the directory.
        filename_to_keep (str): The name of the file to keep.
    
    Returns:
        str: Success message or error message if an error occurs.
    """
    try:
        if os.path.exists(dir):
            for item in os.listdir(dir):
                item_path = os.path.join(dir, item)

                if item == filename_to_keep:
                    continue
                
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.unlink(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
    except Exception as e:
        return f"An error occurred: {e}"


def create_dir(folder_path):
    """
    Create a directory if it does not exist.
    
    Args:
        folder_path (str): The path to the directory to create.
    
    Prints an error message if directory creation fails.
    """
    try:
        os.makedirs(folder_path, exist_ok=True)
    except Exception as e:
        print(f"Error creating dir: {e}")


def find_sv_files(paths: list) -> list:
    """
    Find all SystemVerilog (.sv, .svh) files in the specified directories.
    
    Args:
        paths (list): A list of directory paths to search.
    
    Returns:
        list: A list of paths to .sv and .svh files found in the specified directories.
    """
    sv_files = []
    for path in paths:
        if os.path.exists(path) and os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.endswith('.sv') or file.endswith('.svh'):
                        sv_files.append(os.path.join(root, file))
    return sv_files


def print_dash_line(char='-'):
    """
    Print a line of dash characters based on the terminal width.
    
    Args:
        char (str): The character to use for the line. Default is '-'.
    """
    columns, _ = shutil.get_terminal_size()
    print(char * (columns - 1))


def get_dash_line(char='-') -> str:
    """
    Get a string of dash characters based on the terminal width.
    
    Args:
        char (str): The character to use for the line. Default is '-'.
    
    Returns:
        str: A string of dash characters matching the terminal width.
    """
    columns, _ = shutil.get_terminal_size()
    return char * (columns - 1)
