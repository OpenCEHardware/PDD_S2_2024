#=======================================================================================================
# Imports
#=======================================================================================================
import os
import yaml
from jinja2 import Template
import random
from enum import Enum

import yaml_reader as yr
import Utils as U
#=======================================================================================================
# Globals
#=======================================================================================================
g_LICENSES_SECTION = """# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0"""
#=======================================================================================================
# Defs
#=======================================================================================================
def gen_verilog_sources(metadata: yr.Metadata) -> str:
    """
    Generate the Verilog source files section of the Makefile.

    Args:
        metadata (yr.Metadata): Metadata containing path information.
    
    Returns:
        str: Formatted string for Verilog sources.
    """
    template_section = ""
    plus = ""

    paths_matrix =  metadata.get_paths_matrix()
    VSSF = paths_matrix[0]
    VSLA = paths_matrix[1]

    if(VSLA != []):
        if(VSLA[0] is not None):
            template_section = "SV_DIRS = "
            for filepath in VSLA:
                # if(filepath != VSLA[-1]):
                #     template_section += filepath + " "
                # else:
                #     template_section += filepath

                if(filepath == VSLA[0]):
                    template_section += f'"{filepath}" \\\n'
                elif(filepath != VSLA[-1]):
                    template_section += f'          "{filepath}" \\\n'
                else:
                    template_section += f'          "{filepath}"'


            template_section += "\n" + """VERILOG_SOURCES = $(foreach dir,$(SV_DIRS),$(shell find $(dir) -type f -name "*.sv"))"""
            plus = "+"

    if(VSSF != []):
        template_section += "VERILOG_SOURCES " + plus + "= "
        for filepath in VSSF:
            if(filepath != VSSF[-1]):
                template_section += filepath + " "
            else:
                template_section += filepath

    return template_section


def gen_verilog_includes(metadata: yr.Metadata) -> str:
    """
    Generate the Verilog include directories section of the Makefile.

    Args:
        metadata (yr.Metadata): Metadata containing path information.
    
    Returns:
        str: Formatted string for Verilog include directories.
    """
    template_section = ""

    paths_matrix =  metadata.get_paths_matrix()
    VIDLA = paths_matrix[3]
    if(VIDLA != []):

        template_section = "VERILOG_INCLUDE_DIRS = "
        for filepath in VIDLA:
            if(filepath != VIDLA[-1]):
                template_section += filepath + " "
            else:
                template_section += filepath

    # print(f"template_section\n{template_section}")
    return template_section


def generate_jinja_template(metadata: yr.Metadata, compile: bool) -> str:
    """
    Generate a Jinja2 template for the Makefile.

    Args:
        metadata (yr.Metadata): Metadata containing configuration details.
    
    Returns:
        str: Rendered Makefile template.
    """
    template = g_LICENSES_SECTION + "\n\n"

    template +="""SIM = {{simulator}}
TOPLEVEL_LANG = verilog""" + "\n"

    template += gen_verilog_sources(metadata) + "\n"

    template += gen_verilog_includes(metadata) + "\n"

    template += """TOPLEVEL = {{verilog_module}}
MODULE = {{template_name}}
COCOTB_HDL_TIMEUNIT = {{timescale}}
COCOTB_HDL_TIMEPRECISION = {{timeprecision}}
"""
    # if compile:
    #     template += "COMPILE_ARGS = --cc"
    
    template += """
VERBOSE ?= 0

all: print_vars sim

print_vars:
ifeq ($(VERBOSE),1)
	@echo "SIM: $(SIM)"
	@echo "TOPLEVEL_LANG: $(TOPLEVEL_LANG)"
	@echo "VERILOG_SOURCES: $(VERILOG_SOURCES)"
	@echo "VERILOG_INCLUDE_DIRS: $(VERILOG_INCLUDE_DIRS)"
	@echo "TOPLEVEL: $(TOPLEVEL)"
	@echo "MODULE: $(MODULE)"
	@echo "COCOTB_HDL_TIMEUNIT: $(COCOTB_HDL_TIMEUNIT)"
	@echo "COCOTB_HDL_TIMEPRECISION: $(COCOTB_HDL_TIMEPRECISION)"
endif

include $(shell cocotb-config --makefiles)/Makefile.sim

# Profiling
SIM_ARGS += -fprofile+perf
DOT_BINARY ?= dot
test_profile.pstat: sim
callgraph.svg: test_profile.pstat
	$(shell cocotb-config --python-bin) -m gprof2dot -f pstats ./$< | $(DOT_BINARY) -Tsvg -o $@
.PHONY: profile
profile:
	COCOTB_ENABLE_PROFILING=1 $(MAKE) callgraph.svg"""

    template_instance = Template(template)

    context = {
        "simulator": metadata.simulator,
        "verilog_module" : metadata.DUT_name,
        "template_name" : metadata.template_name,
        "timescale" : metadata.timescale_magnitude + metadata.timescale_unit,
        "timeprecision" : metadata.timeprecision_magnitude + metadata.timeprecision_unit
    }

    rendered_str = template_instance.render(context)

    # print("""#=======================================================================================================
# Makefile
#=======================================================================================================""")

    # print(rendered_str)
    return rendered_str

def write_template(filename, rendered_str, directory):
    """
    Write the rendered template string to a Makefile.

    Args:
        filename (str): Name of the output file.
        rendered_str (str): The rendered template string.
        directory (str): The directory to write the file to.
    """
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w') as file:
        file.write(rendered_str)

def gen_makefile(metadata: yr.Metadata, compile: bool):
    """
    Generate the Makefile using the provided metadata.

    Args:
        metadata (yr.Metadata): Metadata for generating the Makefile.
    """
    print("Generating Makefile")
    rendered_str = generate_jinja_template(metadata, compile)
    write_template("Makefile", rendered_str, metadata.output_dir)