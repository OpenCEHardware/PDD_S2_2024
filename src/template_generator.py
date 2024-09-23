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


def has_clocks(metadata: yr.Metadata) -> bool:
    try:
        return (metadata.DUT_inputs[0][metadata.Keys.CLOCKS.value] is not None)
    except (IndexError, KeyError):
        return False

def initiate_clocks(metadata: yr.Metadata) -> str:
    clocks_names_list = metadata.DUT_inputs[0][metadata.Keys.CLOCKS.value]
    
    if(len(clocks_names_list) == 1  ):
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

def handle_resets(metadata: yr.Metadata) -> str:
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
    template = """#=======================================================================================================
# Imports
#=======================================================================================================
import cocotb
from cocotb.triggers import Timer
import logging

from cocotb.clock import Clock
from cocotb.triggers import RisingEdge
from cocotb.triggers import FallingEdge

# For cocotb events
# https://docs.cocotb.org/en/stable/triggers.html

from enum import Enum
import random
import time
#=======================================================================================================
# Settings
#=======================================================================================================
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG) # (DEBUG, INFO, WARNING, ERROR, CRITICAL)
#=======================================================================================================
# Globals
#=======================================================================================================
g_time_unit = '{{timescale_unit}}'
SIGNAL_X = -1
SIGNAL_Z = -2
#=======================================================================================================
# Tests
#=======================================================================================================
@cocotb.test()
async def tb_{{DUT_name}}(dut):
    start_time = time.perf_counter()"""

    # Set up clocks section
    if(has_clocks(metadata)):
        template += "\n\n" + initiate_clocks(metadata) + """\n\n{{g_indent}}# Wait some time
    await Timer(100, units='{{timescale_unit}}')"""
        
    # Set up resets section
    if(has_resets(metadata)):
        template += "\n\n" + handle_resets(metadata)

    template += """\n\n{{g_indent}}# Test body\n
    # Set value example
    # dut.{{some_DUT_value}}.value = 0

    # Print example
    logger.info("Hello world")
#=======================================================================================================
# Aux structures
#=======================================================================================================
class State(Enum):
    START  = 0
    IDLE   = 1
    READY  = 2
    FKD_UP = SIGNAL_X

    def get_random_state():
        return random.choice(list(State)).value

    # end index is exclusive
    def get_random_state_contrained(start_index, end_index):
        return random.choice(list(State)[start_index:end_index]).value

# Struct example
class Packet():
    def __init__(self, header, opcode, data, error, state):
        self.header = header
        self.opcode = opcode
        self.data = data
        self.error = error
        self.state = state
    
    def to_bits(self):
        # if self.state == State.FKD_UP.value:
        #     raise ValueError("State FKD_UP cannot be directly represented as a valid integer.")

        packet_value = (self.header << (4 + 64 + 4 + 4)) | \\
                       (self.opcode << (64 + 4 + 4)) | \\
                       (self.data << (4 + 4)) | \\
                       (self.error << 4) | \\
                       self.state
        return packet_value

    def __repr__(self):
            return f"Packet(header={self.header:x}, opcode={self.opcode:x}, data={self.data:x}, error={self.error:x}, state={self.state})"
"""

    if(has_clocks(metadata) or has_resets(metadata)):
        template += """#=======================================================================================================
# Handle secuential signals
#=======================================================================================================
"""

    if(has_clocks(metadata)):
        template += g_CLOCK_FUNCTIONS

    if(has_clocks(metadata) and has_resets(metadata)):
        template += "\n"

    if(has_resets(metadata)):
        template += g_RESET_FUNCTIONS
    
    template +="""#=======================================================================================================
# Aux tasks
#======================================================================================================="""

    if(has_clocks(metadata)):
        template += "\n" + g_CLASS_INSTANCE_USAGE + "\n"
    
    template += """# To get simulation time
def get_real_time(start_time):
    return time.perf_counter() - start_time
"""

    template_instance = Template(template)

    if(has_clocks(metadata)):
        some_clock = metadata.DUT_inputs[0][metadata.Keys.CLOCKS.value][0]
    else:
        some_clock = "some_clock"

    if(has_inputs(metadata)):
        some_value = metadata.DUT_inputs[-1]
    else:
        some_value = "input"

    context = {
        "timescale_unit": metadata.timescale_unit,
        "DUT_name": metadata.DUT_name,
        "g_indent" : g_indent,
        "some_clock" : some_clock,
        "some_DUT_value" : some_value
    }

    rendered_str = template_instance.render(context)
    return rendered_str

def write_template(filename, rendered_str, directory):
    # print(f"metadata.output_dir: {directory}")
    """Writes the python test template."""
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w') as file:
        file.write(rendered_str)

def gen_template(metadata: yr.Metadata):
    U.print_dash_line()
    print("Generating template")
    rendered_str = generate_jinja_template(metadata)
    write_template(f"{metadata.template_name}.py", rendered_str, directory=metadata.output_dir)