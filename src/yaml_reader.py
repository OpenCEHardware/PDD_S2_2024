#=======================================================================================================
# Imports
#=======================================================================================================
import yaml
import os
import sys
import re
from enum import Enum
import Utils as U
from pathlib import Path
#=======================================================================================================
# Defs
#=======================================================================================================
class Metadata:
    """
    Metadata class to manage and validate metadata keys, templates, and configuration data.
    """

    class Keys(Enum):
        OUTPUT_DIR = 'output_dir'
        TEMPLATE_TYPE = "template_type"
        VSAID = 'verilog_sources_and_include_dirs'
        VERILOG_SOURCES = 'verilog_sources'
        SPECIFIC_FILES = 'specific_files'
        LOAD_ALL_FROM = 'load_all_from'
        VERILOG_INCLUDE_DIRS = 'verilog_include_dirs'
        SIMULATOR = 'simulator'
        TIMESCALE_TIMEPRESISION = 'timescale_timeprecision'
        DUT_NAME = 'DUT_name'
        TEMPLATE_NAME = 'template_name'
        DUT_INPUTS = 'DUT_inputs'
        CLOCKS = 'clocks'
        RESETS = 'resets'
        DUT_OUTPUTS = 'DUT_outputs'
        QUARTUS_PROJECT_PATH = 'quartus_project_path'
        SYNTHESIZABILITY_COMMAND = 'synthesizability_command'
        TEST_ERROR_PATTERN = 'test_error'
        TEST_WARNING_PATTERN = 'test_warning'
        GENERAL_ERROR_PATTERN = 'general_error'
        GENERAL_WARNING_PATTERN = 'general_warning'


    class Template_types(Enum):
        SIMPLE = 'simple'
        STRUCTURED = 'structured'


    def __init__(self, yaml):
        """
        Initializes the Metadata class with YAML data.

        Args:
            yaml (dict): Dictionary containing YAML configuration data.
        """
        self.yaml = yaml
        dictionary = self.yaml

        self.output_dir = self._get_required_key(dictionary, self.Keys.OUTPUT_DIR.value)
        self.template_type = self._get_required_key(dictionary, self.Keys.TEMPLATE_TYPE.value)
        self.simulator = self._get_required_key(dictionary, self.Keys.SIMULATOR.value)
        self.timescale_timeprecision = self._parse_timescale(dictionary[self.Keys.TIMESCALE_TIMEPRESISION.value])
        self.DUT_name = self._get_required_key(dictionary, self.Keys.DUT_NAME.value)
        self.template_name = self._get_required_key(dictionary, self.Keys.TEMPLATE_NAME.value)
        self.DUT_inputs = self._get_required_key(dictionary, self.Keys.DUT_INPUTS.value)
        self.DUT_outputs = self._get_required_key(dictionary, self.Keys.DUT_OUTPUTS.value)
        self.quartus_project_path = dictionary.get(Metadata.Keys.QUARTUS_PROJECT_PATH.value)
        self.synthesizability_command = dictionary.get(Metadata.Keys.SYNTHESIZABILITY_COMMAND.value)

        self.test_error_pattern = dictionary.get(Metadata.Keys.TEST_ERROR_PATTERN.value)
        self.test_warning_pattern = dictionary.get(Metadata.Keys.TEST_WARNING_PATTERN.value)
        self.general_error_pattern = dictionary.get(Metadata.Keys.GENERAL_ERROR_PATTERN.value)
        self.general_warning_pattern = dictionary.get(Metadata.Keys.GENERAL_WARNING_PATTERN.value)
    


        if self.is_valid_key(dictionary, self.Keys.VSAID.value):
            d_list = dictionary[self.Keys.VSAID.value]
            self._validate_vsaid_structure(d_list)
            self._load_verilog_data()

        self.verify_all_paths()


    def _get_required_key(self, dictionary, key):
        """
        Helper to fetch required keys from the dictionary.

        Args:
            dictionary (dict): Dictionary from which to fetch the key.
            key (str): Key to retrieve.

        Raises:
            KeyError: If the key is not found in the dictionary.
            ValueError: If the key's value is invalid.

        Returns:
            Any: Value associated with the provided key.
        """
        """Helper to fetch required keys."""
        if key not in dictionary:
            raise KeyError(f"yaml missing key: {key}")
        if not self.is_valid_key(dictionary, key):
            raise ValueError(f"key: {key} value is invalid")
        return dictionary[key]


    def is_dict(self, d) -> bool:
        """
        Checks if a variable is a dictionary.

        Args:
            d (Any): Variable to check.

        Raises:
            TypeError: If `d` is not a dictionary.

        Returns:
            bool: True if `d` is a dictionary.
        """
        if not isinstance(d, dict):
            raise TypeError(f"{d} must be a dictionary")
        return True


    def _parse_timescale(self, timescale_timeprecision):
        """
        Parse and validate the timescale and timeprecision format.

        Args:
            timescale_timeprecision (str): Timescale and timeprecision string.

        Raises:
            ValueError: If the timescale format is invalid.
        """
        """Parse and validate the timescale and timeprecision."""
        pattern = r'(\d+)(\w+)/(\d+)(\w+)'
        match = re.search(pattern, timescale_timeprecision)
        if match:
            self.timescale_magnitude = match.group(1)
            self.timescale_unit = match.group(2)
            self.timeprecision_magnitude = match.group(3)
            self.timeprecision_unit = match.group(4)

            if not all([self.timeprecision_magnitude, self.timescale_unit, self.timeprecision_magnitude, self.timeprecision_unit]):
                raise ValueError(f"Some time values are empty")
        else:
            raise ValueError(f"String {timescale_timeprecision} does not have match")


    def _validate_vsaid_structure(self, d_list):
        """
        Ensure the verilog_sources_and_include_dirs structure is valid.

        Args:
            d_list (list): List to validate.

        Raises:
            ValueError: If the structure does not match expectations.
            TypeError: If elements are not dictionaries.
        """
        """Ensure the verilog_sources_and_include_dirs structure is valid."""
        if not isinstance(d_list, list) or len(d_list) != 2:
            raise ValueError(f"VSAID must be a list with 2 elements")
        if not all(isinstance(d, dict) for d in d_list):
            raise TypeError("Both elements in VSAID must be dictionaries")


    def _load_verilog_data(self):
        """
        Load Verilog sources and include directories from YAML data.
        """
        """Load verilog sources and include directories."""
        verilog_data = self.yaml.get('verilog_sources_and_include_dirs', [])
        aux = [[],[],[],[]]

        # verilog_data = [d,d]
        verilog_sources = verilog_data[0][Metadata.Keys.VERILOG_SOURCES.value] # [d,d]

        specific_files = verilog_sources[0].get(Metadata.Keys.SPECIFIC_FILES.value, []) # []
        specific_files = specific_files if specific_files else []
        aux[0] = specific_files

        load_all_from = verilog_sources[1].get(Metadata.Keys.LOAD_ALL_FROM.value, []) # []
        load_all_from = load_all_from if load_all_from else []
        aux[1] = load_all_from
    
        verilog_include_dirs = verilog_data[1][Metadata.Keys.VERILOG_INCLUDE_DIRS.value] # [d,d]

        specific_files = verilog_include_dirs[0].get(Metadata.Keys.SPECIFIC_FILES.value, []) # []
        specific_files = specific_files if specific_files else []
        aux[2] = specific_files

        load_all_from = verilog_include_dirs[1].get(Metadata.Keys.LOAD_ALL_FROM.value, []) # []
        load_all_from = load_all_from if load_all_from else []
        aux[3] = load_all_from

        self.verilog_sources_specific_files = aux[0]
        self.verilog_sources_load_all_from = aux[1]
        self.verilog_include_dirs_specific_files = aux[2]
        self.verilog_include_dirs_load_all_from = aux[3]

    def is_valid_key(self, d, k, nullable=False) -> bool:
        """
        Check if a key is valid and not None.

        Args:
            d (dict): Dictionary to check.
            k (str): Key to validate.
            nullable (bool, optional): If True, allows None values.

        Raises:
            ValueError: If key is missing or invalid.

        Returns:
            bool: True if the key is valid.
        """
        """Check if a key is valid and not None."""
        if k not in d or (d[k] is None and not nullable):
            raise ValueError(f"key: {k} value is invalid")
        return True


    def load_paths(self, d, k) -> list:
        """
        Load paths from a dictionary key, ensuring it's a list.

        Args:
            d (dict): Dictionary to search.
            k (str): Key to load paths from.

        Returns:
            list: List of paths or empty list.
        """
        if self.is_valid_key(d, k) and isinstance(d[k], list):
            return d[k]
        return []


    def verify_all_paths(self) -> bool:
        """
        Verify the existence and validity of various paths.

        Returns:
            bool: True if all paths are valid.
        """        
        path = Path(self.output_dir)
        if not path.is_dir():
            path.mkdir(parents=True, exist_ok=True)

        self._verify_path_list(self.verilog_sources_specific_files, file_check=True)
        self._verify_path_list(self.verilog_sources_load_all_from, dir_check=True)
        self._verify_path_list(self.verilog_include_dirs_specific_files, file_check=True)
        self._verify_path_list(self.verilog_include_dirs_load_all_from, dir_check=True)

        if not any([self.verilog_sources_specific_files, self.verilog_sources_load_all_from]):
            raise ValueError("Modules not found")

        # self._verify_quartus_project()

        return True


    def _verify_path_list(self, path_list, file_check=False, dir_check=False):
        """
        Verify a list of paths are either files or directories.

        Args:
            path_list (list): List of paths to check.
            file_check (bool, optional): Check paths as files if True.
            dir_check (bool, optional): Check paths as directories if True.

        Raises:
            ValueError: If a path is invalid.
        """
        try:
            for path in path_list:
                path = Path(path)
                if file_check and not path.is_file():
                    raise ValueError(f"The path {path} is not a valid file")
                if dir_check and not path.is_dir():
                    raise ValueError(f"The path {path} is not a valid directory")
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit()


    def _verify_quartus_project(self):
        """Verify the Quartus project path is a valid directory."""

        try:

            quartus_path = Path(self.quartus_project_path)
            if not quartus_path.is_dir():    
                raise ValueError(f"The Quartus project path {self.quartus_project_path} is not a valid directory")

        except ValueError as e:

            print(f"Error: {e}")
            sys.exit()


    def get_paths_matrix(self):
        """
        Retrieve a matrix of paths based on the operating system.

        Returns:
            List[List[str]]: Nested list of Verilog source and include paths, adjusted for WSL if on Windows.
        """
        if(U.g_os_name == U.OS.WINDOWS.value):
            return self.get_converted_to_WSL_paths_matrix()
        else:
            return \
                    [
                        self.verilog_sources_specific_files,
                        self.verilog_sources_load_all_from,
                        self.verilog_include_dirs_specific_files,
                        self.verilog_include_dirs_load_all_from
                    ]


    def get_converted_to_WSL_paths_matrix(self):
        """
        Convert Windows paths to WSL format.

        Returns:
            List[List[str]]: Matrix of converted paths for WSL.
        """
        result = [[],[],[],[]]
        for i in range(len(self.verilog_sources_specific_files)):
            result[0].append(U.windows_to_wsl_path(self.verilog_sources_specific_files[i]))

        for i in range(len(self.verilog_sources_load_all_from)):
            result[1].append(U.windows_to_wsl_path(self.verilog_sources_load_all_from[i]))

        for i in range(len(self.verilog_include_dirs_specific_files)):
            result[2].append(U.windows_to_wsl_path(self.verilog_include_dirs_specific_files[i]))

        for i in range(len(self.verilog_include_dirs_load_all_from)):
            result[3].append(U.windows_to_wsl_path(self.verilog_include_dirs_load_all_from[i]))
        return result


    def get_combined_path_list(self) -> list:
        """
        Display the metadata attributes in a formatted output.
        """
        return self.verilog_sources_specific_files + self.verilog_sources_load_all_from + self.verilog_include_dirs_specific_files + self.verilog_include_dirs_load_all_from


    def display(self):
        print(f"Output Directory: {self.output_dir}")
        print(f"Template type: {self.template_type}")
        print(f"Verilog sources specific files: {self.verilog_sources_specific_files}")
        print(f"Verilog sources load all from: {self.verilog_sources_load_all_from}")
        print(f"Verilog include dirs specific files: {self.verilog_include_dirs_specific_files}")
        print(f"Verilog include dirs load all from: {self.verilog_include_dirs_load_all_from}")
        print(f"Simulator: {self.simulator}")
        print(f"Timescale: {self.timescale_magnitude}{self.timescale_unit}, type: {type(self.timescale_magnitude)} and {type(self.timescale_unit)}")
        print(f"Timeprecision: {self.timeprecision_magnitude}{self.timeprecision_unit}, type: {type(self.timeprecision_magnitude)} and {type(self.timeprecision_unit)}")
        print(f"DUT Name: {self.DUT_name}")
        print(f"Template Name: {self.template_name}")
        print(f"DUT Inputs: {self.DUT_inputs}")
        print(f"DUT Outputs: {self.DUT_outputs}")
        print(f"Quartus Project Path: {self.quartus_project_path}")


def read_yaml(yaml_filepath):
    """
    Read a YAML file and return a Metadata instance.

    Args:
        yaml_filepath (str): Path to the YAML file.

    Returns:
        Metadata: Metadata object initialized with YAML data.

    Raises:
        FileNotFoundError: If the YAML file is not found.
        ValueError: If the YAML data is not a dictionary.
    """
    print("Reading YAML")

    yaml_dic = None
    try:
        with open(yaml_filepath, 'r') as file:
            yaml_dic = yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Error: {e}")
        sys.exit()


    if not isinstance(yaml_dic, dict):
        raise ValueError("yaml_dic must be a valid dictionary")
    
    return Metadata(yaml_dic)
