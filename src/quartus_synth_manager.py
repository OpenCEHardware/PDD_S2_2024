#=======================================================================================================
# Imports
#=======================================================================================================
import subprocess
import shutil
import os
import sys

import yaml_reader as yr
import Utils as U
import reporter as rep
#=======================================================================================================
# Defs
#=======================================================================================================
def find_quartus_project_names(project_path: str) -> tuple:
    """
    Find the Quartus project names based on the provided project path.
    
    This function checks for the existence of both .qpf and .qsf files in the specified 
    project directory. If both files are found, it returns their names without extensions.
    
    Args:
        project_path (str): The path to the Quartus project directory.
    
    Returns:
        tuple: A tuple containing the names of the .qpf and .qsf files (without extensions).
    
    Raises:
        SystemExit: If the project path is not found or does not contain both required files.
    """
    try:
        project_names = {}

        for file in os.listdir(project_path):

            if file.endswith(".qpf") or file.endswith(".qsf"):

                project_name = os.path.splitext(file)[0]
                project_names[file.endswith(".qpf")] = project_name
        
        # Check if both files are present
        if all(project_names.values()):
            return project_names[True], project_names[False]  # return (qpf_name, qsf_name)
        
        else:
            raise FileNotFoundError("Both .qpf and .qsf files must exist in the project directory.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit()



def mod_qsf(metadata: yr.Metadata, qsf_filepath, top_level_entity: str):
    with open(qsf_filepath, 'r') as file:
        lines = file.readlines()

    top_level_line = [i for i, line in enumerate(lines) if "TOP_LEVEL_ENTITY" in line]

    if top_level_line:
        lines[top_level_line[0]] = f"set_global_assignment -name TOP_LEVEL_ENTITY {top_level_entity}\n"
    else:
        lines.append(f"set_global_assignment -name TOP_LEVEL_ENTITY {top_level_entity}\n")

    lines.append("\n\n\n")

    sv_files = U.find_sv_files(metadata.get_combined_path_list())
    for sv in sv_files:
        # lines.append(f'set_global_assignment -name VERILOG_FILE {sv}\n')
        lines.append(f'set_global_assignment -name SOURCE_FILE "{U.windows_to_unix_path(sv)}"\n')
 
    # for line in lines:
    #     print(line)

    with open(qsf_filepath, 'w') as file:
        file.writelines(lines)


def run_quartus_compile(metadata: yr.Metadata ,project_path, qpf_file_name):

    if metadata.synthesizability_command:
        command = metadata.synthesizability_command
    else:
        command = f"quartus_sh --flow compile {qpf_file_name}"

    print(f"Running command: {command}")
    U.print_dash_line()

    try:
    
        result = subprocess.run(command, cwd=project_path, check=True, shell=True, capture_output=True, text=True)
        rep.log(metadata, result=result, source=rep.Sources.QUARTUS)

        U.print_dash_line()
        print("Quartus command completed successfully.")

    except subprocess.CalledProcessError as e:

        U.print_dash_line()
        print(f"Error executing Quartus command: {e}")


def restore_qsf(qsf_filepath):
    shutil.copy(qsf_filepath + ".bak", qsf_filepath)
    # print("Archivo .qsf restaurado a su estado original.")


def handle_quartus_synthesis(metadata: yr.Metadata):

    qpf_file_name, qsf_file_name = find_quartus_project_names(project_path=metadata.quartus_project_path)
    qsf_filepath = os.path.join(metadata.quartus_project_path, f"{qsf_file_name}.qsf")
    top_level_entity = metadata.DUT_name
    project_path = metadata.quartus_project_path
    
    shutil.copy(qsf_filepath, qsf_filepath + ".bak")
    mod_qsf(metadata, qsf_filepath, top_level_entity)
    run_quartus_compile(metadata ,project_path, qpf_file_name)
    restore_qsf(qsf_filepath)