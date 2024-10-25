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
    WINDOWS  = "Windows"
    UBUNTU   = "Ubuntu"

class SIM(Enum):
    VERILATOR = "Verilator"
    QUESTA   = "Questa"

class COMMAND_RECEIVER(Enum):
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
    global g_TEMPLATE_OPTION_0, g_TEMPLATE_OPTION_1, g_TEMPLATE_STRUCTURE_OPTION_0, g_output_dir, g_sim_build_dir
    if(g_os_name == OS.UBUNTU.value):
        g_TEMPLATE_OPTION_0 = windows_to_unix_path(g_TEMPLATE_OPTION_0)
        g_TEMPLATE_OPTION_1 = windows_to_unix_path(g_TEMPLATE_OPTION_1)
        g_TEMPLATE_STRUCTURE_OPTION_0 = windows_to_unix_path(g_TEMPLATE_STRUCTURE_OPTION_0)
        g_output_dir = windows_to_unix_path(g_output_dir)
        g_sim_build_dir = windows_to_unix_path(g_sim_build_dir)

def windows_to_unix_path(windows_path):
    return windows_path.replace('\\', '/')


def windows_to_wsl_path(windows_path):
    wsl_path = windows_to_unix_path(windows_path)
    
    if wsl_path[1:3] == ':/' or wsl_path[1:2] == ':':
        drive_letter = wsl_path[0].lower()
        wsl_path = f'/mnt/{drive_letter}{wsl_path[2:]}'    
    return wsl_path


def is_directory_empty(dir_path):
    """Check if the specified directory is empty."""
    return not os.listdir(dir_path)


def file_exists(file_name, dir):
    file_path = os.path.join(dir, file_name)
    return os.path.isfile(file_path)


def set_output_dirs_from_metadata(metadata):
    global g_output_dir, g_sim_build_dir, g_reports_dir
    g_output_dir = metadata.output_dir
    g_sim_build_dir = os.path.join(g_output_dir, g_sim_build_dir)
    g_reports_dir = os.path.join(g_output_dir, g_reports_dir)


def write_to_txt(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        return "File written successfully."
    except Exception as e:
        return f"An error occurred: {e}"


def read_from_txt(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"
    

def clear_directory(directory_path):
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
    try:
        os.makedirs(folder_path, exist_ok=True)
    except Exception as e:
        print(f"Error creating dir: {e}")


def find_sv_files(paths: list) -> list:
    sv_files = []
    for path in paths:
        if os.path.exists(path) and os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.endswith('.sv') or file.endswith('.svh'):
                        sv_files.append(os.path.join(root, file))
    return sv_files

def print_dash_line(char='-'):
    columns, _ = shutil.get_terminal_size()
    print(char * (columns - 1))

def get_dash_line(char='-') -> str:
    columns, _ = shutil.get_terminal_size()
    return char * (columns - 1)
