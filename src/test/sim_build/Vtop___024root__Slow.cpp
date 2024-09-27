// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See Vtop.h for the primary calling header

#include "Vtop__pch.h"
#include "Vtop__Syms.h"
#include "Vtop___024root.h"

// Parameter definitions for Vtop___024root
constexpr IData/*31:0*/ Vtop___024root::ALU_RV32I__DOT__N;
constexpr IData/*31:0*/ Vtop___024root::ALU_RV32I__DOT__add_sub__DOT__N;
constexpr IData/*31:0*/ Vtop___024root::ALU_RV32I__DOT__add_sub__DOT__a1__DOT__N;
constexpr IData/*31:0*/ Vtop___024root::ALU_RV32I__DOT__add_sub__DOT__adder__DOT__N;
constexpr IData/*31:0*/ Vtop___024root::ALU_RV32I__DOT__slt__DOT__N;
constexpr IData/*31:0*/ Vtop___024root::ALU_RV32I__DOT__slt__DOT__adder__DOT__N;
constexpr IData/*31:0*/ Vtop___024root::ALU_RV32I__DOT__abs__DOT__N;
constexpr IData/*31:0*/ Vtop___024root::ALU_RV32I__DOT__abs__DOT__add__DOT__N;
constexpr IData/*31:0*/ Vtop___024root::ALU_RV32I__DOT__abs__DOT__mux__DOT__M;
constexpr IData/*31:0*/ Vtop___024root::ALU_RV32I__DOT__abs__DOT__mux__DOT__N;
constexpr IData/*31:0*/ Vtop___024root::ALU_RV32I__DOT__mux__DOT__M;
constexpr IData/*31:0*/ Vtop___024root::ALU_RV32I__DOT__mux__DOT__N;


void Vtop___024root___ctor_var_reset(Vtop___024root* vlSelf);

Vtop___024root::Vtop___024root(Vtop__Syms* symsp, const char* v__name)
    : VerilatedModule{v__name}
    , vlSymsp{symsp}
 {
    // Reset structure values
    Vtop___024root___ctor_var_reset(this);
}

void Vtop___024root::__Vconfigure(bool first) {
    (void)first;  // Prevent unused variable warning
}

Vtop___024root::~Vtop___024root() {
}
