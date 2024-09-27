"""
This module generates makefiles.
"""
import os
import yaml
from jinja2 import Template
import random
from enum import Enum

import yaml_reader as yr
import Utils as U

g_LICENSES_SECTION = """# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0"""




def gen_verilog_sources(metadata: yr.Metadata) -> str:
    template_section = ""
    plus = ""

    if(metadata.verilog_sources_load_all_from != []):
        if(metadata.verilog_sources_load_all_from[0] is not None):
            template_section = "SV_DIRS = "
            for filepath in metadata.verilog_sources_load_all_from:
                if(filepath != metadata.verilog_sources_load_all_from[-1]):
                    template_section += filepath + " "
                else:
                    template_section += filepath

            template_section += "\n" + """VERILOG_SOURCES = $(foreach dir,$(SV_DIRS),$(shell find $(dir) -type f -name "*.sv"))"""
            plus = "+"

    if(metadata.verilog_sources_specific_files != []):
        template_section += "VERILOG_SOURCES " + plus + "= "
        for filepath in metadata.verilog_sources_specific_files:
            if(filepath != metadata.verilog_sources_specific_files[-1]):
                template_section += filepath + " "
            else:
                template_section += filepath
    return template_section


def gen_verilog_includes(metadata: yr.Metadata) -> str:
    template_section = ""
    if(metadata.verilog_include_dirs_load_all_from != []):

        template_section = "VERILOG_INCLUDE_DIRS = "
        for filepath in metadata.verilog_include_dirs_load_all_from:
            if(filepath != metadata.verilog_include_dirs_load_all_from[-1]):
                template_section += filepath + " "
            else:
                template_section += filepath

    # print(f"template_section\n{template_section}")
    return template_section


def generate_jinja_template(metadata: yr.Metadata) -> str:
    template = g_LICENSES_SECTION + "\n\n"

    template +="""SIM = {{simulator}}
TOPLEVEL_LANG = verilog""" + "\n"

    template += gen_verilog_sources(metadata) + "\n"

    template += gen_verilog_includes(metadata) + "\n"

    template += """TOPLEVEL = {{verilog_module}}
MODULE = {{template_name}}
COCOTB_HDL_TIMEUNIT = {{timescale}}
COCOTB_HDL_TIMEPRECISION = {{timeprecision}}

VERBOSE ?= 0

all: print_vars sim

print_vars:
ifeq ($(VERBOSE),1)
	@echo "Running make..."
	@echo "SIM: $(SIM)"
	@echo "TOPLEVEL_LANG: $(TOPLEVEL_LANG)"
	@echo "VERILOG_SOURCES: $(VERILOG_SOURCES)"
	@echo "VERILOG_INCLUDE_DIRS: $(VERILOG_INCLUDE_DIRS)"
	@echo "TOPLEVEL: $(TOPLEVEL)"
	@echo "MODULE: $(MODULE)"
	@echo "COCOTB_HDL_TIMEUNIT: $(COCOTB_HDL_TIMEUNIT)"
	@echo "COCOTB_HDL_TIMEPRECISION: $(COCOTB_HDL_TIMEPRECISION)"
endif

include $(shell cocotb-config --makefiles)/Makefile.sim"""

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
    """Writes the makefile."""
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w') as file:
        file.write(rendered_str)

def gen_makefile(metadata: yr.Metadata):
    U.print_dash_line()
    print("Generating Makefile")
    rendered_str = generate_jinja_template(metadata)
    write_template("Makefile", rendered_str, metadata.output_dir)