# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0

SIM = verilator
TOPLEVEL_LANG = verilog
SV_DIRS = /mnt/d/D/TEC/2024/S2/Proyecto_de_diseno/Pruebas/modules
VERILOG_SOURCES = $(foreach dir,$(SV_DIRS),$(shell find $(dir) -type f -name "*.sv"))
VERILOG_INCLUDE_DIRS = /mnt/d/D/TEC/2024/S2/Proyecto_de_diseno/Pruebas/module_dependencies
TOPLEVEL = generic_fifo
MODULE = tb_generic_fifo
COCOTB_HDL_TIMEUNIT = 1ns
COCOTB_HDL_TIMEPRECISION = 1ps

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

include $(shell cocotb-config --makefiles)/Makefile.sim