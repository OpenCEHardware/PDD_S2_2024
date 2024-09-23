# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0

# Makefile

SIM ?= verilator

TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += $(PWD)/generic_fifo.sv
VERILOG_SOURCES += $(PWD)/utils_pkg.svh

# COCOTB_TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = generic_fifo

# COCOTB_TEST_MODULES is the basename of the Python test file(s)
MODULE = tb_generic_fifo

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim