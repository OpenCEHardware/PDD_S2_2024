// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design internal header
// See Vtop.h for the primary calling header

#ifndef VERILATED_VTOP___024ROOT_H_
#define VERILATED_VTOP___024ROOT_H_  // guard

#include "verilated.h"


class Vtop__Syms;

class alignas(VL_CACHE_LINE_BYTES) Vtop___024root final : public VerilatedModule {
  public:

    // DESIGN SPECIFIC STATE
    VL_IN8(aclk,0,0);
    VL_IN8(resetn,0,0);
    VL_IN8(push,0,0);
    VL_IN8(pop,0,0);
    VL_OUT8(rd_ptr,0,0);
    VL_OUT8(wr_ptr,0,0);
    VL_OUT8(empty,0,0);
    VL_OUT8(full,0,0);
    CData/*0:0*/ generic_fifo__DOT__aclk;
    CData/*0:0*/ generic_fifo__DOT__resetn;
    CData/*0:0*/ generic_fifo__DOT__push;
    CData/*0:0*/ generic_fifo__DOT__pop;
    CData/*0:0*/ generic_fifo__DOT__rd_ptr;
    CData/*0:0*/ generic_fifo__DOT__wr_ptr;
    CData/*0:0*/ generic_fifo__DOT__empty;
    CData/*0:0*/ generic_fifo__DOT__full;
    CData/*1:0*/ generic_fifo__DOT__count;
    CData/*0:0*/ __VstlFirstIteration;
    CData/*0:0*/ __VicoFirstIteration;
    CData/*0:0*/ __Vtrigprevexpr___TOP__aclk__0;
    CData/*0:0*/ __VactContinue;
    IData/*31:0*/ generic_fifo__DOT__unnamedblk1__DOT__i;
    IData/*31:0*/ __VactIterCount;
    VL_INW(data_in,83,0,3);
    VL_OUTW(data_out,83,0,3);
    VlWide<3>/*83:0*/ generic_fifo__DOT__data_in;
    VlWide<3>/*83:0*/ generic_fifo__DOT__data_out;
    VlUnpacked<VlWide<3>/*83:0*/, 2> generic_fifo__DOT__mem;
    VlTriggerVec<1> __VstlTriggered;
    VlTriggerVec<1> __VicoTriggered;
    VlTriggerVec<1> __VactTriggered;
    VlTriggerVec<1> __VnbaTriggered;

    // INTERNAL VARIABLES
    Vtop__Syms* const vlSymsp;

    // PARAMETERS
    static constexpr IData/*31:0*/ generic_fifo__DOT__DEPTH = 2U;
    static constexpr IData/*31:0*/ generic_fifo__DOT__COUNT_SIZE = 1U;

    // CONSTRUCTORS
    Vtop___024root(Vtop__Syms* symsp, const char* v__name);
    ~Vtop___024root();
    VL_UNCOPYABLE(Vtop___024root);

    // INTERNAL METHODS
    void __Vconfigure(bool first);
};


#endif  // guard
