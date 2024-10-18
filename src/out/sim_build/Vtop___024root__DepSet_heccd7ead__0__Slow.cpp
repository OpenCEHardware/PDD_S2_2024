// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See Vtop.h for the primary calling header

#include "Vtop__pch.h"
#include "Vtop___024root.h"

VL_ATTR_COLD void Vtop___024root___eval_static(Vtop___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_static\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
}

VL_ATTR_COLD void Vtop___024root___eval_initial__TOP(Vtop___024root* vlSelf);

VL_ATTR_COLD void Vtop___024root___eval_initial(Vtop___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_initial\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
    // Body
    Vtop___024root___eval_initial__TOP(vlSelf);
}

VL_ATTR_COLD void Vtop___024root___eval_initial__TOP(Vtop___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_initial__TOP\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
    // Body
    vlSelfRef.ALU_RV32I__DOT__slt__DOT__adder__DOT__ci = 1U;
    vlSelfRef.ALU_RV32I__DOT__abs__DOT__add__DOT__B = 0U;
}

VL_ATTR_COLD void Vtop___024root___eval_final(Vtop___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_final\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
}

#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__stl(Vtop___024root* vlSelf);
#endif  // VL_DEBUG
VL_ATTR_COLD bool Vtop___024root___eval_phase__stl(Vtop___024root* vlSelf);

VL_ATTR_COLD void Vtop___024root___eval_settle(Vtop___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_settle\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
    // Init
    IData/*31:0*/ __VstlIterCount;
    CData/*0:0*/ __VstlContinue;
    // Body
    __VstlIterCount = 0U;
    vlSelfRef.__VstlFirstIteration = 1U;
    __VstlContinue = 1U;
    while (__VstlContinue) {
        if (VL_UNLIKELY((0x64U < __VstlIterCount))) {
#ifdef VL_DEBUG
            Vtop___024root___dump_triggers__stl(vlSelf);
#endif
            VL_FATAL_MT("/mnt/d/D/Files/program_works/Logic_Circuit/Processors/RISCV/Quartus/CE4302-Project-II-main/cpu/Modules/RV32I/ALU_RV32I.sv", 1, "", "Settle region did not converge.");
        }
        __VstlIterCount = ((IData)(1U) + __VstlIterCount);
        __VstlContinue = 0U;
        if (Vtop___024root___eval_phase__stl(vlSelf)) {
            __VstlContinue = 1U;
        }
        vlSelfRef.__VstlFirstIteration = 0U;
    }
}

#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__stl(Vtop___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___dump_triggers__stl\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if ((1U & (~ vlSelfRef.__VstlTriggered.any()))) {
        VL_DBG_MSGF("         No triggers active\n");
    }
    if ((1ULL & vlSelfRef.__VstlTriggered.word(0U))) {
        VL_DBG_MSGF("         'stl' region trigger index 0 is active: Internal 'stl' trigger - first iteration\n");
    }
}
#endif  // VL_DEBUG

void Vtop___024root___ico_sequent__TOP__0(Vtop___024root* vlSelf);

VL_ATTR_COLD void Vtop___024root___eval_stl(Vtop___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_stl\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if ((1ULL & vlSelfRef.__VstlTriggered.word(0U))) {
        Vtop___024root___ico_sequent__TOP__0(vlSelf);
    }
}

VL_ATTR_COLD void Vtop___024root___eval_triggers__stl(Vtop___024root* vlSelf);

VL_ATTR_COLD bool Vtop___024root___eval_phase__stl(Vtop___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_phase__stl\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
    // Init
    CData/*0:0*/ __VstlExecute;
    // Body
    Vtop___024root___eval_triggers__stl(vlSelf);
    __VstlExecute = vlSelfRef.__VstlTriggered.any();
    if (__VstlExecute) {
        Vtop___024root___eval_stl(vlSelf);
    }
    return (__VstlExecute);
}

#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__ico(Vtop___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___dump_triggers__ico\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if ((1U & (~ vlSelfRef.__VicoTriggered.any()))) {
        VL_DBG_MSGF("         No triggers active\n");
    }
    if ((1ULL & vlSelfRef.__VicoTriggered.word(0U))) {
        VL_DBG_MSGF("         'ico' region trigger index 0 is active: Internal 'ico' trigger - first iteration\n");
    }
}
#endif  // VL_DEBUG

#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__act(Vtop___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___dump_triggers__act\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if ((1U & (~ vlSelfRef.__VactTriggered.any()))) {
        VL_DBG_MSGF("         No triggers active\n");
    }
}
#endif  // VL_DEBUG

#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__nba(Vtop___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___dump_triggers__nba\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if ((1U & (~ vlSelfRef.__VnbaTriggered.any()))) {
        VL_DBG_MSGF("         No triggers active\n");
    }
}
#endif  // VL_DEBUG

VL_ATTR_COLD void Vtop___024root___ctor_var_reset(Vtop___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___ctor_var_reset\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
    // Body
    vlSelf->op = VL_RAND_RESET_I(4);
    vlSelf->a = VL_RAND_RESET_I(4);
    vlSelf->b = VL_RAND_RESET_I(4);
    vlSelf->o = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__op = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__a = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__b = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__o = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__add_sub_o = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__a_signed_for_shift_right_arithmetic = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__slt_o = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__abs_o = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__add_sub__DOT__op = VL_RAND_RESET_I(1);
    vlSelf->ALU_RV32I__DOT__add_sub__DOT__a = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__add_sub__DOT__b = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__add_sub__DOT__o = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__add_sub__DOT__b_a1 = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__add_sub__DOT__a1__DOT__a = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__add_sub__DOT__a1__DOT__on = VL_RAND_RESET_I(1);
    vlSelf->ALU_RV32I__DOT__add_sub__DOT__a1__DOT__a1 = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__add_sub__DOT__adder__DOT__ci = VL_RAND_RESET_I(1);
    vlSelf->ALU_RV32I__DOT__add_sub__DOT__adder__DOT__A = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__add_sub__DOT__adder__DOT__B = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__add_sub__DOT__adder__DOT__O = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__slt__DOT__unsigned_ = VL_RAND_RESET_I(1);
    vlSelf->ALU_RV32I__DOT__slt__DOT__a = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__slt__DOT__b = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__slt__DOT__o = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__slt__DOT__adder_o = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__slt__DOT__co = VL_RAND_RESET_I(1);
    vlSelf->ALU_RV32I__DOT__slt__DOT__o_aux = VL_RAND_RESET_I(1);
    vlSelf->ALU_RV32I__DOT__slt__DOT__adder__DOT__ci = VL_RAND_RESET_I(1);
    vlSelf->ALU_RV32I__DOT__slt__DOT__adder__DOT__A = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__slt__DOT__adder__DOT__B = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__slt__DOT__adder__DOT__O = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__slt__DOT__adder__DOT__co = VL_RAND_RESET_I(1);
    vlSelf->ALU_RV32I__DOT__abs__DOT__A = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__abs__DOT__abs_A = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__abs__DOT__adder_o = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__abs__DOT__add__DOT__ci = VL_RAND_RESET_I(1);
    vlSelf->ALU_RV32I__DOT__abs__DOT__add__DOT__A = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__abs__DOT__add__DOT__B = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__abs__DOT__add__DOT__O = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__abs__DOT__mux__DOT__select = VL_RAND_RESET_I(1);
    vlSelf->ALU_RV32I__DOT__abs__DOT__mux__DOT__channels = VL_RAND_RESET_I(8);
    vlSelf->ALU_RV32I__DOT__abs__DOT__mux__DOT__channel_out = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__mux__DOT__select = VL_RAND_RESET_I(4);
    vlSelf->ALU_RV32I__DOT__mux__DOT__channels = VL_RAND_RESET_Q(64);
    vlSelf->ALU_RV32I__DOT__mux__DOT__channel_out = VL_RAND_RESET_I(4);
}
