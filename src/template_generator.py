"""
This module generates templates.
Offers functions to get random hexadecimal values, read yaml files, generate jinja templates and write files.
"""
import os
import yaml
from jinja2 import Template
import random
from enum import Enum

import yaml_reader as yr


import Utils as U


yr.Metadata

g_metadata = False
g_DEFAULT_CLOCK_PERIOD_TIME_MAGNITUDE = 10
g_DEFAULT_RESET_START_MAGNITUDE = 0
g_DEFAULT_RESET_DURATION_MAGNITUDE = 10

g_indent_level = 4
g_indent = ' ' * g_indent_level


g_SECUENTIAL_FUNCTIONS_HEADER = """#=======================================================================================================
# Handle secuential signals
#=======================================================================================================
"""
g_CLOCK_FUNCTIONS = """async def start_clock(clock, period, units='{{timescale_unit}}'):
        clock_instance = Clock(clock, period, units=units)
        cocotb.start_soon(clock_instance.start())

async def start_all_clocks(clocks, period, units='{{timescale_unit}}'):
        for clock in clocks:
            cocotb.start_soon(start_clock(clock, period, units))
"""
g_RESET_FUNCTIONS = """async def reset_signal(reset, start, duration, units='{{timescale_unit}}'):
    await Timer(start, units)
    reset.value = 0
    await Timer(duration, units)
    reset.value = 1

async def reset_all(resets, start, duration, units='{{timescale_unit}}'):
    for reset in resets:
        cocotb.start_soon(reset_signal(reset, start, duration, units))
"""
g_CLASS_INSTANCE_USAGE = """# Handle class instance example
async def set_input(dut, packet):
    await RisingEdge(dut.{{some_clock}})
    dut.push.value = 1
    dut.data_in <= packet.to_bits()

    await RisingEdge(dut.{{some_clock}})
    dut.push.value = 0

    for _ in range(5):
        await RisingEdge(dut.{{some_clock}})

async def get_output(dut, packet):
    await RisingEdge(dut.{{some_clock}})
    dut.pop.value = 1
    packet = dut.data_out.value

    await RisingEdge(dut.{{some_clock}})
    dut.pop.value = 0

    for _ in range(5):
        await RisingEdge(dut.{{some_clock}})
"""



def has_inputs(metadata: yr.Metadata) -> bool:
    try:
        return (metadata.DUT_inputs[2] is not None)
    except (IndexError, KeyError):
        return False

def has_outputs(metadata: yr.Metadata) -> bool:
    try:
        return (metadata.DUT_outputs[0] is not None)
    except (IndexError, KeyError):
        return False

def has_clocks(metadata: yr.Metadata) -> bool:
    try:
        return (metadata.DUT_inputs[0][metadata.Keys.CLOCKS.value] is not None)
    except (IndexError, KeyError):
        return False

def get_initiate_clocks_section(metadata: yr.Metadata) -> str:
    clocks_names_list = metadata.DUT_inputs[0][metadata.Keys.CLOCKS.value]
    
    if(len(clocks_names_list) == 1):
        template_section = f"{g_indent}# Initiate clock\n"
        template_section += f"{g_indent}await start_clock(dut.{clocks_names_list[0]}, period={g_DEFAULT_CLOCK_PERIOD_TIME_MAGNITUDE}, units='{metadata.timescale_unit}')"

    elif(len(clocks_names_list) > 1):
        template_section = f"{g_indent}# Initiate clocks\n"
        template_section += f"{g_indent}clocks = ["

        last_index = len(clocks_names_list) - 1
        for i, clock_name in enumerate(clocks_names_list):
            if i != last_index:
                template_section += f"dut.{clock_name}, "
            else:
                template_section += f"dut.{clock_name}"
        template_section += "]\n"
        template_section += f"{g_indent}await start_all_clocks(clocks, period={g_DEFAULT_CLOCK_PERIOD_TIME_MAGNITUDE}, units='{metadata.timescale_unit}')"

    return template_section

def has_resets(metadata: yr.Metadata) -> bool:
    try:
        return (metadata.DUT_inputs[1][metadata.Keys.RESETS.value] is not None)
    except (IndexError, KeyError):
        return False

def get_handle_resets_section(metadata: yr.Metadata) -> str:
    resets_names_list = metadata.DUT_inputs[1][metadata.Keys.RESETS.value]
    
    if(len(resets_names_list) == 1):
        template_section = f"{g_indent}# Reset\n"
        template_section += f"{g_indent}await reset_signal(dut.{resets_names_list[0]}, start={g_DEFAULT_RESET_START_MAGNITUDE}, duration={g_DEFAULT_RESET_DURATION_MAGNITUDE}, units='{metadata.timescale_unit}')"

    elif(len(resets_names_list) > 1):
        template_section = f"{g_indent}# Resets\n"
        template_section += f"{g_indent}resets = ["

        last_index = len(resets_names_list) - 1
        for i, reset_name in enumerate(resets_names_list):
            if i != last_index:
                template_section += f"dut.{reset_name}, "
            else:
                template_section += f"dut.{reset_name}"
        template_section += "]\n"
        template_section += f"{g_indent}await reset_all(resets, start={g_DEFAULT_RESET_START_MAGNITUDE}, duration={g_DEFAULT_RESET_DURATION_MAGNITUDE}, units='{metadata.timescale_unit}')"

    return template_section


def generate_jinja_template(metadata: yr.Metadata, template_option) -> str:
    has_clocks_ = has_clocks(metadata)
    has_resets_ = has_resets(metadata)
    has_inputs_ = has_inputs(metadata)
    has_outputs_ = has_outputs(metadata)
    add_structure_example = True

    template = ''
    setup_clocks_section = ''
    setup_resets_section = ''
    structure_example_section = ''
    secuential_functions_header_section = ''
    clocks_functions_section = ''
    resets_functions_section = ''
    some_clock = ''
    some_DUT_input = ''
    some_DUT_output = ''

    if(template_option == metadata.Template_types.SIMPLE.value):
        with open(U.g_TEMPLATE_OPTION_0, 'r') as file:
            lines = file.readlines()
        template = ''.join(lines)
    if(template_option == metadata.Template_types.STRUCTURED.value):
        with open(U.g_TEMPLATE_OPTION_1, 'r') as file:
            lines = file.readlines()
        template = ''.join(lines)

    if(has_clocks_):
        setup_clocks_section = get_initiate_clocks_section(metadata)
        clocks_functions_section += g_CLOCK_FUNCTIONS
        some_clock = metadata.DUT_inputs[0][metadata.Keys.CLOCKS.value][0]
    else:
        some_clock = "some_clock"

    if(has_resets_):
        setup_resets_section += "\n\n" + get_handle_resets_section(metadata)
        resets_functions_section += g_RESET_FUNCTIONS

    if(add_structure_example):
        with open(U.windows_to_unix_path(U.g_TEMPLATE_STRUCTURE_OPTION_0), 'r') as file:
            lines = file.readlines()
        structure_example_section = ''.join(lines)

    if(has_clocks_ or has_resets_):
        secuential_functions_header_section = g_SECUENTIAL_FUNCTIONS_HEADER

    if(has_clocks_ and has_resets_):
        template += "\n"

    template_instance = Template(template)

    if(has_inputs_):
        some_DUT_input = metadata.DUT_inputs[-1]
    else:
        some_DUT_input = "some_input"

    if(has_outputs_):
        some_DUT_output = metadata.DUT_outputs[0]
    else:
        some_DUT_output = "some_output"

    context = {
        "timescale_unit": metadata.timescale_unit,
        "DUT_name": metadata.DUT_name,
        "g_indent" : g_indent,
        "setup_clocks_section" : setup_clocks_section,
        "setup_resets_section" : setup_resets_section,
        "structure_example_section" : structure_example_section,
        "secuential_functions_header_section" : secuential_functions_header_section,
        "clocks_functions_section" : clocks_functions_section,
        "resets_functions_section" : resets_functions_section,
        "some_clock" : some_clock,
        "some_DUT_input" : some_DUT_input,
        "some_DUT_output" : some_DUT_output
    }

    rendered_str = template_instance.render(context)
    return rendered_str

def write_template(filename, rendered_str, directory):
    """Writes the python test template."""
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w') as file:
        file.write(rendered_str)

def gen_template(metadata: yr.Metadata, template_option):
    U.print_dash_line()
    print("Generating template")
    rendered_str = generate_jinja_template(metadata, template_option)
    write_template(f"{metadata.template_name}.py", rendered_str, directory=metadata.output_dir)