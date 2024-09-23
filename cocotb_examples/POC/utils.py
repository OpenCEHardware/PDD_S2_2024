import cocotb
from cocotb.triggers import Timer
from cocotb.clock import Clock


g_unit = "ps"

def set_unit(value):
    global g_unit
    g_unit = value

def generate_clock(dut_clock_name, dut_clock_level_time):
    clock = Clock(dut_clock_name, dut_clock_level_time*2, units=g_unit)
    cocotb.start_soon(clock.start())  # start the clock

async def wait(magnitude, unit=g_unit):
    await Timer(magnitude, units=unit)

# ================================================================================================================
### Examples
# ================================================================================================================
## -- Prints --

# Needs:

# import logging
# Needs settings as:
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG) # (DEBUG, INFO, WARNING, ERROR, CRITICAL)

# Usage:

# logger.info()
# ================================================================================================================
## -- Asignation --
# dut.input.value = some_value
# ================================================================================================================
## -- Wait simulation time --

# Needs:

# from cocotb.triggers import Timer

# Usage:

# await Timer(100, units="ns")
# ================================================================================================================
## -- Assert --

# Needs:

# from cocotb.result import TestError

# Usage:

# if dut.signal.value != expected_value:
#     raise TestFailure(f"Test failed: expected value: {expected_value} is diferent to {dut.signal.value}")
# ================================================================================================================
## -- Wait for clock event (rising edge) --

# Needs:

# from cocotb.triggers import RisingEdge

# Usage:

# # Captures first raising edge
# await RisingEdge(dut.clk)

# # Apply stimulus like
# dut.signal <= 1

# # Waits for another raising edge
# await RisingEdge(dut.clk)

# # Apply stimulus like
# dut.signal <= 0
# ================================================================================================================
## -- Wait for clock event (falling edge) --

# Needs:

# from cocotb.triggers import FallingEdge

# Usage:

# # Captures first raising edge
# await FallingEdge(dut.clk)

# # Apply stimulus like
# dut.signal <= 1

# # Captures another falling edge
# await FallingEdge(dut.clk)

# # Apply stimulus like
# dut.signal <= 0
# ================================================================================================================
## -- Wait for clock event (any edge) --

# Needs:

# from cocotb.triggers import Edge

# Usage:

# # Captures first edge
# await Edge(dut.clk)

# # Apply stimulus like
# dut.signal <= 1
# ================================================================================================================
## -- Wait for clock event (clock cycles) --

# Needs:

# from cocotb.triggers import ClockCycles

# Usage:

# # Wait 10 cycles
# await ClockCycles(dut.clk, 10)

# # Apply stimulus like
# dut.signal <= 1
# ================================================================================================================
## -- Wait for clock event (any event) --

# Needs:

# from cocotb.triggers import Any, RisingEdge, Timer

# Usage:

# # Waits for a rising egde or 50 ns, whatever happens first
# await Any(RisingEdge(dut.clk), Timer(50, units='ns'))

# # Apply stimulus like
# dut.signal <= 1
# ================================================================================================================
## -- Wait for custom event --

# Needs:

# from cocotb.triggers import Event

# Usage:

# my_event = Event()

# @cocotb.test()
# async def event_test(dut):
#     # Some logic to setup the event
#     my_event.set()
    
#     # Waits for the event
#     await my_event.wait()

#     # Apply stimulus like
#     dut.signal <= 1
# ================================================================================================================