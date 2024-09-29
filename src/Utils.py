import shutil
import os
import platform
from enum import Enum


class OS(Enum):
    WINDOWS  = "Windows"
    UBUNTU   = "Ubuntu"


g_os_name = OS.WINDOWS.value

# Windows default format
g_TEMPLATE_OPTION_0 = '..\\templates\\arch_simple.txt'
g_TEMPLATE_OPTION_1 = '..\\templates\\arch_structured.txt'
g_TEMPLATE_STRUCTURE_OPTION_0 = '..\\templates\\structure_example_1.txt'
g_TEST_PATH = "test"
g_SIM_BUILD_PATH = "test\\sim_build"
g_QUESTA_BIN_PATH = "/root/intelFPGA_pro/23.1/questa_fse/bin"


def recognize_os():
    global g_os_name
    current_os = os.name

    if current_os == 'posix':
        if platform.system() == "Linux" and "ubuntu" in platform.version().lower():
            g_os_name = OS.UBUNTU.value
            covert_template_paths()


def covert_template_paths():
    global g_TEMPLATE_OPTION_0, g_TEMPLATE_OPTION_1, g_TEMPLATE_STRUCTURE_OPTION_0, g_TEST_PATH, g_SIM_BUILD_PATH
    if(g_os_name == OS.UBUNTU.value):
        g_TEMPLATE_OPTION_0 = windows_to_unix_path(g_TEMPLATE_OPTION_0)
        g_TEMPLATE_OPTION_1 = windows_to_unix_path(g_TEMPLATE_OPTION_1)
        g_TEMPLATE_STRUCTURE_OPTION_0 = windows_to_unix_path(g_TEMPLATE_STRUCTURE_OPTION_0)
        g_TEST_PATH = windows_to_unix_path(g_TEST_PATH)
        g_SIM_BUILD_PATH = windows_to_unix_path(g_SIM_BUILD_PATH)

def covert_metadata_path(path):
    if(g_os_name == OS.WINDOWS.value):
        return windows_to_wsl_path(path)


def print_dash_line(char='-'):
    columns, _ = shutil.get_terminal_size()
    print(char * (columns - 1))


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