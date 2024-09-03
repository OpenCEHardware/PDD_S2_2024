#=======================================================================================================
# Imports
import cocotb
from cocotb.triggers import Timer
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge
import logging

from enum import Enum
import random
import time
#=======================================================================================================
# Settings
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG) # (DEBUG, INFO, WARNING, ERROR, CRITICAL)
#=======================================================================================================
# Globals
g_time_unit = "ns"
SIGNAL_X = -1
SIGNAL_Z = -2
#=======================================================================================================
# Tests
@cocotb.test()
async def tb_generic_fifo(dut):
    start_time = time.perf_counter()

    # -- Set DUT clocks --
    # Creates a clock (50% duty)
    clock = Clock(dut.aclk, 10, units="ns")
    # Starts clock
    cocotb.start_soon(clock.start())

    # Is optional to wait some time before continue
    await Timer(100, units='ns')

    await reset(dut, 50, 100)
    await Timer(300, g_time_unit)

    packet = Packet(header=0,opcode=0,data=0,error=0,state=State.FKD_UP.value)

    for _ in range(12):
        packet.header = 0xFF
        packet.opcode = 0xA
        packet.data = 0xDEAFDEADDEAFDEAD
        packet.error = 0xE
        packet.state = State.get_random_state()

        logger.info(packet.__repr__)
        await set_input(dut, packet)

    for _ in range(5):
        await get_output(dut, packet)
        logger.info(f" wr_ptr = {dut.wr_ptr} | rd_ptr = {dut.rd_ptr} | {get_real_time(start_time)}")
        logger.info(f" packet = {packet.__repr__}")

    for _ in range(10):
        packet.header = 0xAA
        packet.opcode = 0xB
        packet.data = 0x0000DEADDEAF0000
        packet.error = 0xC
        packet.state = State.get_random_state_contrained(1, 3)

        logger.info(packet.__repr__)
        await set_input(dut, packet)

    for _ in range(5):
        await get_output(dut, packet)
        logger.info(f" wr_ptr = {dut.wr_ptr} | rd_ptr = {dut.rd_ptr} | {get_real_time(start_time)}")
        logger.info(f" packet = {packet.__repr__}")
#=======================================================================================================
# Aux structures
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

class Packet():
    def __init__(self, header, opcode, data, error, state):
        self.header = header
        self.opcode =  opcode
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
# Aux tasks
async def reset(dut, start, duration):
    await Timer(start, g_time_unit)
    dut.resetn.value = 0

    await Timer(duration, g_time_unit)
    dut.resetn.value = 1
    dut.resetn._log.debug("Reset complete")

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

def get_real_time(start_time):
    return time.perf_counter() - start_time