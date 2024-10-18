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
    VL_IN8(op,3,0);
    VL_IN8(a,3,0);
    VL_IN8(b,3,0);
    VL_OUT8(o,3,0);
    CData/*3:0*/ ALU_RV32I__DOT__op;
    CData/*3:0*/ ALU_RV32I__DOT__a;
    CData/*3:0*/ ALU_RV32I__DOT__b;
    CData/*3:0*/ ALU_RV32I__DOT__o;
    CData/*3:0*/ ALU_RV32I__DOT__add_sub_o;
    CData/*3:0*/ ALU_RV32I__DOT__a_signed_for_shift_right_arithmetic;
    CData/*3:0*/ ALU_RV32I__DOT__slt_o;
    CData/*3:0*/ ALU_RV32I__DOT__abs_o;
    CData/*0:0*/ ALU_RV32I__DOT__add_sub__DOT__op;
    CData/*3:0*/ ALU_RV32I__DOT__add_sub__DOT__a;
    CData/*3:0*/ ALU_RV32I__DOT__add_sub__DOT__b;
    CData/*3:0*/ ALU_RV32I__DOT__add_sub__DOT__o;
    CData/*3:0*/ ALU_RV32I__DOT__add_sub__DOT__b_a1;
    CData/*3:0*/ ALU_RV32I__DOT__add_sub__DOT__a1__DOT__a;
    CData/*0:0*/ ALU_RV32I__DOT__add_sub__DOT__a1__DOT__on;
    CData/*3:0*/ ALU_RV32I__DOT__add_sub__DOT__a1__DOT__a1;
    CData/*0:0*/ ALU_RV32I__DOT__add_sub__DOT__adder__DOT__ci;
    CData/*3:0*/ ALU_RV32I__DOT__add_sub__DOT__adder__DOT__A;
    CData/*3:0*/ ALU_RV32I__DOT__add_sub__DOT__adder__DOT__B;
    CData/*3:0*/ ALU_RV32I__DOT__add_sub__DOT__adder__DOT__O;
    CData/*0:0*/ ALU_RV32I__DOT__slt__DOT__unsigned_;
    CData/*3:0*/ ALU_RV32I__DOT__slt__DOT__a;
    CData/*3:0*/ ALU_RV32I__DOT__slt__DOT__b;
    CData/*3:0*/ ALU_RV32I__DOT__slt__DOT__o;
    CData/*3:0*/ ALU_RV32I__DOT__slt__DOT__adder_o;
    CData/*0:0*/ ALU_RV32I__DOT__slt__DOT__co;
    CData/*0:0*/ ALU_RV32I__DOT__slt__DOT__o_aux;
    CData/*0:0*/ ALU_RV32I__DOT__slt__DOT__adder__DOT__ci;
    CData/*3:0*/ ALU_RV32I__DOT__slt__DOT__adder__DOT__A;
    CData/*3:0*/ ALU_RV32I__DOT__slt__DOT__adder__DOT__B;
    CData/*3:0*/ ALU_RV32I__DOT__slt__DOT__adder__DOT__O;
    CData/*0:0*/ ALU_RV32I__DOT__slt__DOT__adder__DOT__co;
    CData/*3:0*/ ALU_RV32I__DOT__abs__DOT__A;
    CData/*3:0*/ ALU_RV32I__DOT__abs__DOT__abs_A;
    CData/*3:0*/ ALU_RV32I__DOT__abs__DOT__adder_o;
    CData/*0:0*/ ALU_RV32I__DOT__abs__DOT__add__DOT__ci;
    CData/*3:0*/ ALU_RV32I__DOT__abs__DOT__add__DOT__A;
    CData/*3:0*/ ALU_RV32I__DOT__abs__DOT__add__DOT__B;
    CData/*3:0*/ ALU_RV32I__DOT__abs__DOT__add__DOT__O;
    CData/*0:0*/ ALU_RV32I__DOT__abs__DOT__mux__DOT__select;
    CData/*7:0*/ ALU_RV32I__DOT__abs__DOT__mux__DOT__channels;
    CData/*3:0*/ ALU_RV32I__DOT__abs__DOT__mux__DOT__channel_out;
    CData/*3:0*/ ALU_RV32I__DOT__mux__DOT__select;
    QData/*63:0*/ ALU_RV32I__DOT__mux__DOT__channels;
    CData/*3:0*/ ALU_RV32I__DOT__mux__DOT__channel_out;
    CData/*0:0*/ __VstlFirstIteration;
    CData/*0:0*/ __VicoFirstIteration;
    CData/*0:0*/ __VactContinue;
    IData/*31:0*/ __VactIterCount;
    VlTriggerVec<1> __VstlTriggered;
    VlTriggerVec<1> __VicoTriggered;
    VlTriggerVec<0> __VactTriggered;
    VlTriggerVec<0> __VnbaTriggered;

    // INTERNAL VARIABLES
    Vtop__Syms* const vlSymsp;

    // PARAMETERS
    static constexpr IData/*31:0*/ ALU_RV32I__DOT__N = 4U;
    static constexpr IData/*31:0*/ ALU_RV32I__DOT__add_sub__DOT__N = 4U;
    static constexpr IData/*31:0*/ ALU_RV32I__DOT__add_sub__DOT__a1__DOT__N = 4U;
    static constexpr IData/*31:0*/ ALU_RV32I__DOT__add_sub__DOT__adder__DOT__N = 4U;
    static constexpr IData/*31:0*/ ALU_RV32I__DOT__slt__DOT__N = 4U;
    static constexpr IData/*31:0*/ ALU_RV32I__DOT__slt__DOT__adder__DOT__N = 4U;
    static constexpr IData/*31:0*/ ALU_RV32I__DOT__abs__DOT__N = 4U;
    static constexpr IData/*31:0*/ ALU_RV32I__DOT__abs__DOT__add__DOT__N = 4U;
    static constexpr IData/*31:0*/ ALU_RV32I__DOT__abs__DOT__mux__DOT__M = 2U;
    static constexpr IData/*31:0*/ ALU_RV32I__DOT__abs__DOT__mux__DOT__N = 4U;
    static constexpr IData/*31:0*/ ALU_RV32I__DOT__mux__DOT__M = 0x00000010U;
    static constexpr IData/*31:0*/ ALU_RV32I__DOT__mux__DOT__N = 4U;

    // CONSTRUCTORS
    Vtop___024root(Vtop__Syms* symsp, const char* v__name);
    ~Vtop___024root();
    VL_UNCOPYABLE(Vtop___024root);

    // INTERNAL METHODS
    void __Vconfigure(bool first);
};


#endif  // guard
