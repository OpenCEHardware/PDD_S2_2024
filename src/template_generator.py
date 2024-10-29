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
    """
    Checks if the provided metadata has any inputs defined.

    This function attempts to access the third element of the DUT_inputs list 
    in the metadata. If it exists and is not None, the function returns True. 
    If there is an IndexError or KeyError, it returns False.

    Args:
        metadata (yr.Metadata): The metadata object containing DUT inputs information.

    Returns:
        bool: True if inputs are defined; otherwise, False.
    """
    try:
        return (metadata.DUT_inputs[2] is not None)
    except (IndexError, KeyError):
        return False


def has_outputs(metadata: yr.Metadata) -> bool:
    """
    Checks if the provided metadata has any outputs defined.

    This function attempts to access the first element of the DUT_outputs list 
    in the metadata. If it exists and is not None, the function returns True. 
    If there is an IndexError or KeyError, it returns False.

    Args:
        metadata (yr.Metadata): The metadata object containing DUT outputs information.

    Returns:
        bool: True if outputs are defined; otherwise, False.
    """
    try:
        return (metadata.DUT_outputs[0] is not None)
    except (IndexError, KeyError):
        return False


def has_clocks(metadata: yr.Metadata) -> bool:
    """
    Checks if the provided metadata has any clock signals defined.

    This function attempts to access the clock signals in the first element 
    of the DUT_inputs list using the CLOCKS key from the Keys enumeration. 
    If it exists and is not None, the function returns True. 
    If there is an IndexError or KeyError, it returns False.

    Args:
        metadata (yr.Metadata): The metadata object containing DUT input information.

    Returns:
        bool: True if clock signals are defined; otherwise, False.
    """
    try:
        return (metadata.DUT_inputs[0][metadata.Keys.CLOCKS.value] is not None)
    except (IndexError, KeyError):
        return False


def get_initiate_clocks_section(metadata: yr.Metadata) -> str:
    """
    Generates a section of code to initiate clock signals based on the provided metadata.

    This function retrieves the clock names from the DUT_inputs of the metadata. 
    If there is one clock, it generates a line to start that clock. If there are 
    multiple clocks, it generates a list of clocks and a line to start all of them.

    Args:
        metadata (yr.Metadata): The metadata object containing DUT input information.

    Returns:
        str: The generated code section for initiating clocks.
    """
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
    """
    Checks if the provided metadata has any reset signals defined.

    This function attempts to access the resets defined in the DUT_inputs of the 
    metadata. If the resets list exists and is not None, it returns True. If 
    there is an IndexError or KeyError, it returns False.

    Args:
        metadata (yr.Metadata): The metadata object containing DUT input information.

    Returns:
        bool: True if resets are defined; otherwise, False.
    """
    try:
        return (metadata.DUT_inputs[1][metadata.Keys.RESETS.value] is not None)
    except (IndexError, KeyError):
        return False

def get_handle_resets_section(metadata: yr.Metadata) -> str:
    """
    Generates a section of code to handle reset signals based on the provided metadata.

    This function retrieves the reset names from the DUT_inputs of the metadata. 
    If there is one reset, it generates a line to reset that signal. If there are 
    multiple resets, it generates a list of resets and a line to reset all of them.

    Args:
        metadata (yr.Metadata): The metadata object containing DUT input information.

    Returns:
        str: The generated code section for handling resets.
    """
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


def generate_jinja_template(metadata: yr.Metadata) -> str:
    """
    Generates a Jinja template string based on the provided metadata.

    This function constructs a template for testing a hardware design under test (DUT)
    by checking the existence of clocks, resets, inputs, and outputs in the metadata. 
    It includes sections for setting up clocks and resets, as well as generating 
    function headers and examples based on the template type specified in the metadata.

    Args:
        metadata (yr.Metadata): The metadata object containing DUT information and configuration.

    Returns:
        str: The rendered Jinja template string for the DUT test.
    """
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

    if(metadata.template_type == metadata.Template_types.SIMPLE.value):
        with open(U.g_TEMPLATE_OPTION_0, 'r') as file:
            lines = file.readlines()
        template = ''.join(lines)
    if(metadata.template_type == metadata.Template_types.STRUCTURED.value):
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

    context = \
    {
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
    """
    Writes a rendered template string to a specified file.

    This function creates a file with the specified filename in the given directory 
    and writes the rendered template string to it.

    Args:
        filename (str): The name of the file to write the template to.
        rendered_str (str): The rendered template string to write to the file.
        directory (str): The directory where the file will be created.
    """
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w') as file:
        file.write(rendered_str)


def gen_template(metadata: yr.Metadata):
    """
    Generates and writes a test template for the DUT.

    This function generates a Jinja template string using the provided metadata,
    then writes it to a file named after the template_name specified in the metadata.

    Args:
        metadata (yr.Metadata): The metadata object containing DUT information and output directory.
    """
    print("Generating template")
    rendered_str = generate_jinja_template(metadata)
    write_template(f"{metadata.template_name}.py", rendered_str, directory=metadata.output_dir)