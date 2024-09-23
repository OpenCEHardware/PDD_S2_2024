// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Symbol table implementation internals

#include "Vtop__pch.h"
#include "Vtop.h"
#include "Vtop___024root.h"
#include "Vtop___024unit.h"

// FUNCTIONS
Vtop__Syms::~Vtop__Syms()
{

    // Tear down scope hierarchy
    __Vhier.remove(0, &__Vscope_generic_fifo);
    __Vhier.remove(&__Vscope_generic_fifo, &__Vscope_generic_fifo__unnamedblk1);

}

Vtop__Syms::Vtop__Syms(VerilatedContext* contextp, const char* namep, Vtop* modelp)
    : VerilatedSyms{contextp}
    // Setup internal state of the Syms class
    , __Vm_modelp{modelp}
    // Setup module instances
    , TOP{this, namep}
{
        // Check resources
        Verilated::stackCheck(61);
    // Configure time unit / time precision
    _vm_contextp__->timeunit(-9);
    _vm_contextp__->timeprecision(-12);
    // Setup each module's pointers to their submodules
    // Setup each module's pointer back to symbol table (for public functions)
    TOP.__Vconfigure(true);
    // Setup scopes
    __Vscope_TOP.configure(this, name(), "TOP", "TOP", 0, VerilatedScope::SCOPE_OTHER);
    __Vscope_generic_fifo.configure(this, name(), "generic_fifo", "generic_fifo", -9, VerilatedScope::SCOPE_MODULE);
    __Vscope_generic_fifo__unnamedblk1.configure(this, name(), "generic_fifo.unnamedblk1", "unnamedblk1", -9, VerilatedScope::SCOPE_OTHER);

    // Set up scope hierarchy
    __Vhier.add(0, &__Vscope_generic_fifo);
    __Vhier.add(&__Vscope_generic_fifo, &__Vscope_generic_fifo__unnamedblk1);

    // Setup export functions
    for (int __Vfinal = 0; __Vfinal < 2; ++__Vfinal) {
        __Vscope_TOP.varInsert(__Vfinal,"aclk", &(TOP.aclk), false, VLVT_UINT8,VLVD_IN|VLVF_PUB_RW,0);
        __Vscope_TOP.varInsert(__Vfinal,"data_in", &(TOP.data_in), false, VLVT_WDATA,VLVD_IN|VLVF_PUB_RW,1 ,83,0);
        __Vscope_TOP.varInsert(__Vfinal,"data_out", &(TOP.data_out), false, VLVT_WDATA,VLVD_OUT|VLVF_PUB_RW,1 ,83,0);
        __Vscope_TOP.varInsert(__Vfinal,"empty", &(TOP.empty), false, VLVT_UINT8,VLVD_OUT|VLVF_PUB_RW,0);
        __Vscope_TOP.varInsert(__Vfinal,"full", &(TOP.full), false, VLVT_UINT8,VLVD_OUT|VLVF_PUB_RW,0);
        __Vscope_TOP.varInsert(__Vfinal,"pop", &(TOP.pop), false, VLVT_UINT8,VLVD_IN|VLVF_PUB_RW,0);
        __Vscope_TOP.varInsert(__Vfinal,"push", &(TOP.push), false, VLVT_UINT8,VLVD_IN|VLVF_PUB_RW,0);
        __Vscope_TOP.varInsert(__Vfinal,"rd_ptr", &(TOP.rd_ptr), false, VLVT_UINT8,VLVD_OUT|VLVF_PUB_RW,1 ,0,0);
        __Vscope_TOP.varInsert(__Vfinal,"resetn", &(TOP.resetn), false, VLVT_UINT8,VLVD_IN|VLVF_PUB_RW,0);
        __Vscope_TOP.varInsert(__Vfinal,"wr_ptr", &(TOP.wr_ptr), false, VLVT_UINT8,VLVD_OUT|VLVF_PUB_RW,1 ,0,0);
        __Vscope_generic_fifo.varInsert(__Vfinal,"COUNT_SIZE", const_cast<void*>(static_cast<const void*>(&(TOP.generic_fifo__DOT__COUNT_SIZE))), true, VLVT_UINT32,VLVD_NODIR|VLVF_PUB_RW,1 ,31,0);
        __Vscope_generic_fifo.varInsert(__Vfinal,"DEPTH", const_cast<void*>(static_cast<const void*>(&(TOP.generic_fifo__DOT__DEPTH))), true, VLVT_UINT32,VLVD_NODIR|VLVF_PUB_RW,1 ,31,0);
        __Vscope_generic_fifo.varInsert(__Vfinal,"aclk", &(TOP.generic_fifo__DOT__aclk), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0);
        __Vscope_generic_fifo.varInsert(__Vfinal,"count", &(TOP.generic_fifo__DOT__count), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,1,0);
        __Vscope_generic_fifo.varInsert(__Vfinal,"data_in", &(TOP.generic_fifo__DOT__data_in), false, VLVT_WDATA,VLVD_NODIR|VLVF_PUB_RW,1 ,83,0);
        __Vscope_generic_fifo.varInsert(__Vfinal,"data_out", &(TOP.generic_fifo__DOT__data_out), false, VLVT_WDATA,VLVD_NODIR|VLVF_PUB_RW,1 ,83,0);
        __Vscope_generic_fifo.varInsert(__Vfinal,"empty", &(TOP.generic_fifo__DOT__empty), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0);
        __Vscope_generic_fifo.varInsert(__Vfinal,"full", &(TOP.generic_fifo__DOT__full), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0);
        __Vscope_generic_fifo.varInsert(__Vfinal,"mem", &(TOP.generic_fifo__DOT__mem), false, VLVT_WDATA,VLVD_NODIR|VLVF_PUB_RW,2 ,83,0 ,0,1);
        __Vscope_generic_fifo.varInsert(__Vfinal,"pop", &(TOP.generic_fifo__DOT__pop), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0);
        __Vscope_generic_fifo.varInsert(__Vfinal,"push", &(TOP.generic_fifo__DOT__push), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0);
        __Vscope_generic_fifo.varInsert(__Vfinal,"rd_ptr", &(TOP.generic_fifo__DOT__rd_ptr), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,0,0);
        __Vscope_generic_fifo.varInsert(__Vfinal,"resetn", &(TOP.generic_fifo__DOT__resetn), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0);
        __Vscope_generic_fifo.varInsert(__Vfinal,"wr_ptr", &(TOP.generic_fifo__DOT__wr_ptr), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,0,0);
        __Vscope_generic_fifo__unnamedblk1.varInsert(__Vfinal,"i", &(TOP.generic_fifo__DOT__unnamedblk1__DOT__i), false, VLVT_UINT32,VLVD_NODIR|VLVF_PUB_RW|VLVF_DPI_CLAY,1 ,31,0);
    }
}
