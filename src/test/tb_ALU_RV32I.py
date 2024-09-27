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
async def tb_ALU_RV32I(dut):
    # Wait some time
    await Timer(100, units='ns')

    # Some expected values
    expected_values = [0, 2, 4, 6, 8, 10, 12, 14]
    len_expected_values = len(expected_values)


    scoreboard = Scoreboard()
    scoreboard.expected_values = expected_values




    # Concurrent tasks
    cocotb.start_soon(stimulus_generator(dut.b, len_expected_values))
    # Other inputs
    # cocotb.start_soon(stimulus_generator(dut.other_input, len_expected_values))

    # Some output
    cocotb.start_soon(monitor(dut.o, scoreboard))


    await checker(dut.o, expected_values)
    scoreboard.compare()

#=======================================================================================================
# Verification elements
#=======================================================================================================
@cocotb.coroutine
async def stimulus_generator(dut_input, amount):
    for i in range(amount):
        dut_input.value = i
        await Timer(10, units=g_time_unit)
        # logger.info(f"i = {i}")
        # logger.info(f"{dut_input.name} = {dut_input.value}")

@cocotb.coroutine
async def monitor(dut_output, scoreboard):
    while True:
        await Timer(10, units=g_time_unit)
        output_value = dut_output.value
        scoreboard.add_observed(output_value)

@cocotb.coroutine
async def checker(dut_output, expected_values):
    for expected in expected_values:
        await Timer(10, units=g_time_unit)
        observed = dut_output.value
        assert observed == expected, f"Checker error: observed {observed}, expected {expected}"
        # logger.info(f"observed {observed}, expected {expected}")

class Scoreboard:
    def __init__(self):
        self.expected_values = []
        self.observed_values = []

    def add_expected(self, expected):
        self.expected_values.append(expected)

    def add_observed(self, observed):
        self.observed_values.append(observed)

    def compare(self):
        if len(self.observed_values) > len(self.expected_values):
            self.observed_values = self.observed_values[:len(self.expected_values)]

        assert len(self.observed_values) == len(self.expected_values), (
            f"Error: amount of observed values ({len(self.observed_values)}) doesn't match "
            f"with amount of expected values ({len(self.expected_values)})"
        )
        
        for idx, (obs, exp) in enumerate(zip(self.observed_values, self.expected_values)):
            assert obs == exp, (
                f"Scoreboard error in index {idx}: observed {obs}, expected value {exp}"
            )
        logger.info("Scoreboard: All values match.")
#=======================================================================================================
# Aux structures
#=======================================================================================================
class State(Enum):
    START  = 0
    IDLE   = 1
    READY  = 2
    INCORRECT = SIGNAL_X

    def get_random_state():
        return random.choice(list(State)).value

    # end index is exclusive
    def get_random_state_contrained(start_index, end_index):
        return random.choice(list(State)[start_index:end_index]).value

# Struct example
class Some_class():
    def __init__(self, atribute_1, atribute_2, some_state):
        self.atribute_1 = atribute_1
        self.atribute_2 = atribute_2
        self.some_state = some_state
    
    def to_bits(self):
        # if self.some_state == State.INCORRECT.value:
        #     raise ValueError("State INCORRECT cannot be directly represented as a valid integer.")

        # this example asumes atribute_1 as 4 bits
        # this example asumes atribute_2 as 64 bits
        # this example asumes some_state as 4 bits
        some_class_value = (self.atribute_1 << (64 + 4)) | \
                       (self.atribute_2 << 4) | \
                       self.some_state
        return some_class_value

    def __repr__(self):
            return f"Some_class(atribute 1={self.atribute_1:x}, atribute 2={self.atribute_2:x}, state={self.some_state})"




#=======================================================================================================
# Aux tasks
#=======================================================================================================
# To get simulation time
def get_real_time(start_time):
    return time.perf_counter() - start_time