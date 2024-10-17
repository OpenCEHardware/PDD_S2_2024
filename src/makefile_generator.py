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

    paths_matrix =  metadata.get_paths_matrix()
    VSSF = paths_matrix[0]
    VSLA = paths_matrix[1]

    if(VSLA != []):
        if(VSLA[0] is not None):
            template_section = "SV_DIRS = "
            for filepath in VSLA:
                if(filepath != VSLA[-1]):
                    template_section += filepath + " "
                else:
                    template_section += filepath

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
    print("Generating Makefile")
    rendered_str = generate_jinja_template(metadata)
    write_template("Makefile", rendered_str, metadata.output_dir)