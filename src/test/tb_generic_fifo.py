#=======================================================================================================
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
g_time_unit = 'ns'
SIGNAL_X = -1
SIGNAL_Z = -2
#=======================================================================================================
# Tests
#=======================================================================================================
@cocotb.test()
async def tb_generic_fifo(dut):
    start_time = time.perf_counter()

    # Initiate clock
    await start_clock(dut.aclk, period=10, units='ns')

    # Wait some time
    await Timer(100, units='ns')

    # Reset
    await reset_signal(dut.resetn, start=0, duration=10, units='ns')

    # Test body

    # Set value example
    # dut.pop.value = 0

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

        packet_value = (self.header << (4 + 64 + 4 + 4)) | \
                       (self.opcode << (64 + 4 + 4)) | \
                       (self.data << (4 + 4)) | \
                       (self.error << 4) | \
                       self.state
        return packet_value

    def __repr__(self):
            return f"Packet(header={self.header:x}, opcode={self.opcode:x}, data={self.data:x}, error={self.error:x}, state={self.state})"
#=======================================================================================================
# Handle secuential signals
#=======================================================================================================
async def start_clock(clock, period, units='ns'):
        clock_instance = Clock(clock, period, units=units)
        cocotb.start_soon(clock_instance.start())

async def start_all_clocks(clocks, period, units='ns'):
        for clock in clocks:
            cocotb.start_soon(start_clock(clock, period, units))

async def reset_signal(reset, start, duration, units='ns'):
    await Timer(start, units)
    reset.value = 0
    await Timer(duration, units)
    reset.value = 1

async def reset_all(resets, start, duration, units='ns'):
    for reset in resets:
        cocotb.start_soon(reset_signal(reset, start, duration, units))
#=======================================================================================================
# Aux tasks
#=======================================================================================================
# Handle class instance example
async def set_input(dut, packet):
    await RisingEdge(dut.aclk)
    dut.push.value = 1
    dut.data_in <= packet.to_bits()

    await RisingEdge(dut.aclk)
    dut.push.value = 0

    for _ in range(5):
        await RisingEdge(dut.aclk)

async def get_output(dut, packet):
    await RisingEdge(dut.aclk)
    dut.pop.value = 1
    packet = dut.data_out.value

    await RisingEdge(dut.aclk)
    dut.pop.value = 0

    for _ in range(5):
        await RisingEdge(dut.aclk)

# To get simulation time
def get_real_time(start_time):
    return time.perf_counter() - start_time