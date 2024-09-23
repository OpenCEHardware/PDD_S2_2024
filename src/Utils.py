import shutil


def print_dash_line(char='-'):
    columns, _ = shutil.get_terminal_size()
    print(char * (columns - 1))


def windows_to_wsl_path(windows_path):
    wsl_path = windows_path.replace('\\', '/')
    
    if wsl_path[1:3] == ':/' or wsl_path[1:2] == ':':
        drive_letter = wsl_path[0].lower()
        wsl_path = f'/mnt/{drive_letter}{wsl_path[2:]}'    
    return wsl_path