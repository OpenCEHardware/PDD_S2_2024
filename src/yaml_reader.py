import yaml
import os
import re
from enum import Enum
import Utils as U
from pathlib import Path


class Metadata:
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

    class Template_types(Enum):
        SIMPLE = 'simple'
        STRUCTURED = 'structured'

    def __init__(self, yaml):
        self.yaml = yaml
        # print(f"YAML: {self.yaml}, type: {type(self.yaml)}")

        dictionary = self.yaml

        key = self.Keys.OUTPUT_DIR.value
        if key not in dictionary:
            raise KeyError(f"yaml missing key: {key}")
        else:
            if dictionary[key] is None:
                raise ValueError(f"key: {key} value is invalid")
            else:
                self.output_dir = yaml[key]

        key = self.Keys.TEMPLATE_TYPE.value
        if key not in dictionary:
            raise KeyError(f"yaml missing key: {key}")
        else:
            if dictionary[key] is None:
                raise ValueError(f"key: {key} value is invalid")
            else:
                self.template_type = yaml[key]

        key = self.Keys.VSAID.value
        if(self.valid_key(dictionary, key)):
        
            d_list = dictionary[key]
            if(type(d_list) is not list):
                raise TypeError(f"{key} value must be a list")
            elif(len(d_list) != 2):
                raise ValueError(f"{d_list} must have 2 elements")
            
            else:
                if(self.is_dict(d_list[0]) and self.is_dict(d_list[1])):
                    d_list = [d_list[0], d_list[1]]                   
                    k_list = [self.Keys.VERILOG_SOURCES.value, self.Keys.VERILOG_INCLUDE_DIRS.value]
                    path_lists = self.load_4_list_paths(d_list, k_list)

                    self.verilog_sources_specific_files = path_lists[0][0]
                    self.verilog_sources_load_all_from = path_lists[0][1]
                    self.verilog_include_dirs_specific_files = path_lists[1][0]
                    self.verilog_include_dirs_load_all_from = path_lists[1][1]
                    self.verify_paths()
                    if(U.g_os_name != U.OS.UBUNTU.value):
                        self.convert_paths()


        key = self.Keys.SIMULATOR.value
        if key not in dictionary:
            raise KeyError(f"yaml missing key: {key}")
        else:
            if dictionary[key] is None:
                raise ValueError(f"key: {key} value is invalid")
            else:
                self.simulator = yaml[key]

        timescale_timeprecision=yaml[self.Keys.TIMESCALE_TIMEPRESISION.value]

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

        self.DUT_name = yaml[self.Keys.DUT_NAME.value]
        self.template_name = yaml[self.Keys.TEMPLATE_NAME.value]
        self.DUT_inputs = yaml[self.Keys.DUT_INPUTS.value]
        self.DUT_outputs = yaml[self.Keys.DUT_OUTPUTS.value]


    def is_key(self, d, k):
        if k not in d:
            raise KeyError(f"YAML missing key: {k}")
        return True

    def valid_key(self, d, k) -> bool:
        if(self.is_key(d, k)):
            if d[k] is None:
                raise ValueError(f"key: {k} value is invalid")
        return True

    def load_paths(self, d, k) -> list:
        path_list = []
        if(self.is_key(d, k)):
            value = d[k]
            if value is not None:
                if type(value) is list:
                    path_list = value
        return path_list

    def is_dict(self, d) -> bool:
        if(type(d) is not dict):
            raise TypeError(f"{d} must be a dictionary")
        return True

    def load_2_list_paths(self, d_list, d_keys):
        result = [[],[]]
        d0, d1 = d_list
        if(self.is_dict(d0) and self.is_dict(d1)):
            result[0] = self.load_paths(d0, d_keys[0])
            result[1] = self.load_paths(d1, d_keys[1])
        return result

    def load_4_list_paths(self, d_list, k_list):
        result = []

        for i in range(len(d_list)):
            if(self.valid_key(d_list[i], k_list[i])):
                aux_d_list = d_list[i][k_list[i]]
                if(type(aux_d_list) is not list):
                    raise TypeError(f"{k_list[i]} value must be a list")
                elif(len(aux_d_list) != 2):
                    raise ValueError(f"{aux_d_list} must have 2 elements")                        
                else:
                    aux_d_list = [aux_d_list[0], aux_d_list[1]]
                    aux_k_list = [self.Keys.SPECIFIC_FILES.value, self.Keys.LOAD_ALL_FROM.value]
                    result.append(self.load_2_list_paths(aux_d_list, aux_k_list))
        return result


    def verify_paths(self) -> bool:
        path = Path(self.output_dir)
        if path.is_file():
            raise ValueError(f"The value: {self.output_dir} must be a directory")
        if not path.is_dir():
            path.mkdir(parents=True, exist_ok=True)


        for filepath in self.verilog_sources_specific_files:
            path = Path(filepath)
            if not path.is_file():
                raise ValueError(f"The value {filepath} is not a file")
        for directory in self.verilog_sources_load_all_from:
            path = Path(directory)
            if not path.is_dir():
                raise ValueError(f"The path {directory} is not a directory")
        for filepath in self.verilog_include_dirs_specific_files:
            path = Path(filepath)
            if not path.is_file():
                raise ValueError(f"The value {filepath} is not a file")
        for directory in self.verilog_include_dirs_load_all_from:
            path = Path(directory)
            if not path.is_dir():
                raise ValueError(f"The path {directory} is not a directory")
    
        if(self.verilog_sources_specific_files == [] and self.verilog_sources_load_all_from == []):
            raise ValueError("Modules not found")

        return True

    def convert_paths(self):
        # self.output_dir = U.windows_to_wsl_path(self.output_dir)

        for i in range(len(self.verilog_sources_specific_files)):
            self.verilog_sources_specific_files[i] = U.covert_metadata_path(self.verilog_sources_specific_files[i])

        for i in range(len(self.verilog_sources_load_all_from)):
            self.verilog_sources_load_all_from[i] = U.covert_metadata_path(self.verilog_sources_load_all_from[i])

        for i in range(len(self.verilog_include_dirs_specific_files)):
            self.verilog_include_dirs_specific_files[i] = U.covert_metadata_path(self.verilog_include_dirs_specific_files[i])

        for i in range(len(self.verilog_include_dirs_load_all_from)):
            self.verilog_include_dirs_load_all_from[i] = U.covert_metadata_path(self.verilog_include_dirs_load_all_from[i])


    def has_attribute(self, attr_name):
        return hasattr(self, attr_name) and getattr(self, attr_name) is not None


    def has_any_attribute(self, *attr_names):
        return any(self.has_attribute(attr) for attr in attr_names)


    def has_data_in(self, dictionary, key):
        return (self.find_value(dictionary, key) is not None)


    def display(self):
        print(f"Output Directory: {self.output_dir}, type: {type(self.output_dir)}")
        print(f"Template type: {self.template_type}, type: {type(self.template_type)}")
        print(f"Verilog sources specific files: {self.verilog_sources_specific_files}, type: {type(self.verilog_sources_specific_files)}")
        print(f"Verilog sources load all from: {self.verilog_sources_load_all_from}, type: {type(self.verilog_sources_load_all_from)}")
        print(f"Verilog include dirs specific files: {self.verilog_include_dirs_specific_files}, type: {type(self.verilog_include_dirs_specific_files)}")
        print(f"Verilog include dirs load all from: {self.verilog_include_dirs_load_all_from}, type: {type(self.verilog_include_dirs_load_all_from)}")
        print(f"Simulator: {self.simulator}, type: {type(self.simulator)}")
        print(f"Timescale: {self.timescale_magnitude}{self.timescale_unit}, type: {type(self.timescale_magnitude)} and {type(self.timescale_unit)}")
        print(f"Timeprecision: {self.timeprecision_magnitude}{self.timeprecision_unit}, type: {type(self.timeprecision_magnitude)} and {type(self.timeprecision_unit)}")
        print(f"DUT Name: {self.DUT_name}, type: {type(self.DUT_name)}")
        print(f"Template Name: {self.template_name}, type: {type(self.template_name)}")
        print(f"DUT Inputs: {self.DUT_inputs}, type: {type(self.DUT_inputs)}")
        print(f"DUT Outputs: {self.DUT_outputs}, type: {type(self.DUT_outputs)}")


def read_yaml(yaml_filepath):
    U.print_dash_line()
    print("Reading YAML")

    yaml_dic = None
    try:
        with open(yaml_filepath, 'r') as file:
            yaml_dic = yaml.safe_load(file)
    except:
        raise FileNotFoundError(f"The file {yaml_filepath} was not found.")
    if(type(yaml_dic) != dict):
        raise ValueError("yaml_dic must be a valid dictionary")
    else:
        return Metadata(yaml_dic)
