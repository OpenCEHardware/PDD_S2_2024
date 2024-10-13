// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See Vtop.h for the primary calling header

#include "Vtop__pch.h"
#include "Vtop___024root.h"

void Vtop___024root___ico_sequent__TOP__0(Vtop___024root* vlSelf);

void Vtop___024root___eval_ico(Vtop___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_ico\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if ((1ULL & vlSelfRef.__VicoTriggered.word(0U))) {
        Vtop___024root___ico_sequent__TOP__0(vlSelf);
    }
}

VL_INLINE_OPT void Vtop___024root___ico_sequent__TOP__0(Vtop___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___ico_sequent__TOP__0\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
    // Init
    QData/*63:0*/ ALU_RV32I__DOT____Vcellinp__mux__channels;
    ALU_RV32I__DOT____Vcellinp__mux__channels = 0;
    CData/*7:0*/ ALU_RV32I__DOT__abs__DOT____Vcellinp__mux__channels;
    ALU_RV32I__DOT__abs__DOT____Vcellinp__mux__channels = 0;
    // Body
    vlSelfRef.ALU_RV32I__DOT__slt__DOT__unsigned_ = 
        (1U & ((IData)(vlSelfRef.op) >> 0U));
    vlSelfRef.ALU_RV32I__DOT__slt__DOT__adder__DOT__B 
        = (0xfU & (~ (IData)(vlSelfRef.b)));
    vlSelfRef.ALU_RV32I__DOT__abs__DOT__add__DOT__ci 
        = (1U & ((IData)(vlSelfRef.a) >> 3U));
    vlSelfRef.ALU_RV32I__DOT__abs__DOT__add__DOT__A 
        = (0xfU & (~ (IData)(vlSelfRef.a)));
    vlSelfRef.ALU_RV32I__DOT__abs__DOT__mux__DOT__select 
        = (1U & ((IData)(vlSelfRef.a) >> 3U));
    vlSelfRef.ALU_RV32I__DOT__a_signed_for_shift_right_arithmetic 
        = vlSelfRef.a;
    vlSelfRef.ALU_RV32I__DOT__op = vlSelfRef.op;
    vlSelfRef.ALU_RV32I__DOT__add_sub__DOT__op = (1U 
                                                  & ((IData)(vlSelfRef.op) 
                                                     >> 0U));
    vlSelfRef.ALU_RV32I__DOT__b = vlSelfRef.b;
    vlSelfRef.ALU_RV32I__DOT__a = vlSelfRef.a;
    vlSelfRef.ALU_RV32I__DOT__slt__DOT__adder__DOT__O 
        = (0xfU & ((IData)(1U) + ((~ (IData)(vlSelfRef.b)) 
                                  + (IData)(vlSelfRef.a))));
    vlSelfRef.ALU_RV32I__DOT__slt__DOT__adder__DOT__co 
        = (1U & (((IData)(1U) + ((IData)(vlSelfRef.a) 
                                 + (0xfU & (~ (IData)(vlSelfRef.b))))) 
                 >> 4U));
    if ((1U & (IData)(vlSelfRef.op))) {
        vlSelfRef.ALU_RV32I__DOT__add_sub__DOT__b_a1 
            = (0xfU & (~ (IData)(vlSelfRef.b)));
        vlSelfRef.ALU_RV32I__DOT__slt__DOT__o_aux = 
            (1U & (~ (IData)(vlSelfRef.ALU_RV32I__DOT__slt__DOT__adder__DOT__co)));
    } else {
        vlSelfRef.ALU_RV32I__DOT__add_sub__DOT__b_a1 
            = (0xfU & (IData)(vlSelfRef.b));
        vlSelfRef.ALU_RV32I__DOT__slt__DOT__o_aux = 
            (1U & (((~ ((IData)(vlSelfRef.b) >> 3U)) 
                    & ((IData)(vlSelfRef.a) >> 3U)) 
                   | ((~ (((IData)(vlSelfRef.a) | (IData)(vlSelfRef.b)) 
                          >> 3U)) & ((IData)(vlSelfRef.ALU_RV32I__DOT__slt__DOT__adder__DOT__O) 
                                     >> 3U))));
    }
    vlSelfRef.ALU_RV32I__DOT__abs__DOT__add__DOT__O 
        = (0xfU & (VL_SHIFTR_III(4,4,32, (IData)(vlSelfRef.a), 3U) 
                   + (~ (IData)(vlSelfRef.a))));
    vlSelfRef.ALU_RV32I__DOT__mux__DOT__select = vlSelfRef.ALU_RV32I__DOT__op;
    vlSelfRef.ALU_RV32I__DOT__add_sub__DOT__a1__DOT__on 
        = vlSelfRef.ALU_RV32I__DOT__add_sub__DOT__op;
    vlSelfRef.ALU_RV32I__DOT__add_sub__DOT__adder__DOT__ci 
        = vlSelfRef.ALU_RV32I__DOT__add_sub__DOT__op;
    vlSelfRef.ALU_RV32I__DOT__slt__DOT__b = vlSelfRef.ALU_RV32I__DOT__b;
    vlSelfRef.ALU_RV32I__DOT__add_sub__DOT__b = vlSelfRef.ALU_RV32I__DOT__b;
    vlSelfRef.ALU_RV32I__DOT__abs__DOT__A = vlSelfRef.ALU_RV32I__DOT__a;
    vlSelfRef.ALU_RV32I__DOT__add_sub__DOT__a = vlSelfRef.ALU_RV32I__DOT__a;
    vlSelfRef.ALU_RV32I__DOT__slt__DOT__a = vlSelfRef.ALU_RV32I__DOT__a;
    vlSelfRef.ALU_RV32I__DOT__slt__DOT__adder_o = vlSelfRef.ALU_RV32I__DOT__slt__DOT__adder__DOT__O;
    vlSelfRef.ALU_RV32I__DOT__slt__DOT__co = vlSelfRef.ALU_RV32I__DOT__slt__DOT__adder__DOT__co;
    vlSelfRef.ALU_RV32I__DOT__add_sub__DOT__adder__DOT__B 
        = vlSelfRef.ALU_RV32I__DOT__add_sub__DOT__b_a1;
    vlSelfRef.ALU_RV32I__DOT__add_sub__DOT__a1__DOT__a1 
        = vlSelfRef.ALU_RV32I__DOT__add_sub__DOT__b_a1;
    vlSelfRef.ALU_RV32I__DOT__add_sub__DOT__adder__DOT__O 
        = (0xfU & ((1U & (IData)(vlSelfRef.op)) + ((IData)(vlSelfRef.a) 
                                                   + (IData)(vlSelfRef.ALU_RV32I__DOT__add_sub__DOT__b_a1))));
    vlSelfRef.ALU_RV32I__DOT__abs__DOT__adder_o = vlSelfRef.ALU_RV32I__DOT__abs__DOT__add__DOT__O;
    ALU_RV32I__DOT__abs__DOT____Vcellinp__mux__channels 
        = (((IData)(vlSelfRef.ALU_RV32I__DOT__abs__DOT__add__DOT__O) 
            << 4U) | (IData)(vlSelfRef.a));
    vlSelfRef.ALU_RV32I__DOT__add_sub__DOT__a1__DOT__a 
        = vlSelfRef.ALU_RV32I__DOT__add_sub__DOT__b;
    vlSelfRef.ALU_RV32I__DOT__add_sub__DOT__adder__DOT__A 
        = vlSelfRef.ALU_RV32I__DOT__add_sub__DOT__a;
    vlSelfRef.ALU_RV32I__DOT__slt__DOT__adder__DOT__A 
        = vlSelfRef.ALU_RV32I__DOT__slt__DOT__a;
    vlSelfRef.ALU_RV32I__DOT__slt_o = vlSelfRef.ALU_RV32I__DOT__slt__DOT__o_aux;
    vlSelfRef.ALU_RV32I__DOT__add_sub_o = vlSelfRef.ALU_RV32I__DOT__add_sub__DOT__adder__DOT__O;
    vlSelfRef.ALU_RV32I__DOT__add_sub__DOT__o = vlSelfRef.ALU_RV32I__DOT__add_sub__DOT__adder__DOT__O;
    vlSelfRef.ALU_RV32I__DOT__abs__DOT__mux__DOT__channels 
        = ALU_RV32I__DOT__abs__DOT____Vcellinp__mux__channels;
    vlSelfRef.ALU_RV32I__DOT__abs__DOT__mux__DOT__channel_out 
        = (0xfU & ((IData)(ALU_RV32I__DOT__abs__DOT____Vcellinp__mux__channels) 
                   >> (7U & VL_SHIFTL_III(3,3,32, (1U 
                                                   & ((IData)(vlSelfRef.a) 
                                                      >> 3U)), 2U))));
    vlSelfRef.ALU_RV32I__DOT__slt__DOT__o = vlSelfRef.ALU_RV32I__DOT__slt_o;
    vlSelfRef.ALU_RV32I__DOT__abs_o = vlSelfRef.ALU_RV32I__DOT__abs__DOT__mux__DOT__channel_out;
    vlSelfRef.ALU_RV32I__DOT__abs__DOT__abs_A = vlSelfRef.ALU_RV32I__DOT__abs__DOT__mux__DOT__channel_out;
    ALU_RV32I__DOT____Vcellinp__mux__channels = (((QData)((IData)(
                                                                  (0xfU 
                                                                   & VL_MODDIV_III(4, (IData)(vlSelfRef.a), (IData)(vlSelfRef.b))))) 
                                                  << 0x3cU) 
                                                 | (((QData)((IData)(
                                                                     (0xfU 
                                                                      & VL_DIV_III(4, (IData)(vlSelfRef.a), (IData)(vlSelfRef.b))))) 
                                                     << 0x38U) 
                                                    | (((QData)((IData)(
                                                                        (0xfU 
                                                                         & ((IData)(vlSelfRef.a) 
                                                                            * (IData)(vlSelfRef.b))))) 
                                                        << 0x34U) 
                                                       | (((QData)((IData)(vlSelfRef.ALU_RV32I__DOT__abs__DOT__mux__DOT__channel_out)) 
                                                           << 0x30U) 
                                                          | (((QData)((IData)(vlSelfRef.b)) 
                                                              << 0x2cU) 
                                                             | (((QData)((IData)(vlSelfRef.a)) 
                                                                 << 0x28U) 
                                                                | (((QData)((IData)(
                                                                                (0xffU 
                                                                                & (((IData)(vlSelfRef.ALU_RV32I__DOT__slt_o) 
                                                                                << 4U) 
                                                                                | (IData)(vlSelfRef.ALU_RV32I__DOT__slt_o))))) 
                                                                    << 0x20U) 
                                                                   | (QData)((IData)(
                                                                                ((VL_SHIFTRS_III(4,4,4, (IData)(vlSelfRef.a), (IData)(vlSelfRef.b)) 
                                                                                << 0x1cU) 
                                                                                | ((0xf000000U 
                                                                                & (((IData)(vlSelfRef.a) 
                                                                                >> (IData)(vlSelfRef.b)) 
                                                                                << 0x18U)) 
                                                                                | ((0xf00000U 
                                                                                & (((IData)(vlSelfRef.a) 
                                                                                << (IData)(vlSelfRef.b)) 
                                                                                << 0x14U)) 
                                                                                | ((((IData)(vlSelfRef.a) 
                                                                                & (IData)(vlSelfRef.b)) 
                                                                                << 0x10U) 
                                                                                | ((((IData)(vlSelfRef.a) 
                                                                                | (IData)(vlSelfRef.b)) 
                                                                                << 0xcU) 
                                                                                | ((((IData)(vlSelfRef.a) 
                                                                                ^ (IData)(vlSelfRef.b)) 
                                                                                << 8U) 
                                                                                | (0xffU 
                                                                                & (((IData)(vlSelfRef.ALU_RV32I__DOT__add_sub__DOT__adder__DOT__O) 
                                                                                << 4U) 
                                                                                | (IData)(vlSelfRef.ALU_RV32I__DOT__add_sub__DOT__adder__DOT__O))))))))))))))))));
    vlSelfRef.ALU_RV32I__DOT__mux__DOT__channels = ALU_RV32I__DOT____Vcellinp__mux__channels;
    vlSelfRef.ALU_RV32I__DOT__mux__DOT__channel_out 
        = (0xfU & (IData)((ALU_RV32I__DOT____Vcellinp__mux__channels 
                           >> (0x3fU & VL_SHIFTL_III(6,6,32, (IData)(vlSelfRef.op), 2U)))));
    vlSelfRef.o = vlSelfRef.ALU_RV32I__DOT__mux__DOT__channel_out;
    vlSelfRef.ALU_RV32I__DOT__o = vlSelfRef.ALU_RV32I__DOT__mux__DOT__channel_out;
}

void Vtop___024root___eval_triggers__ico(Vtop___024root* vlSelf);

bool Vtop___024root___eval_phase__ico(Vtop___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_phase__ico\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
    // Init
    CData/*0:0*/ __VicoExecute;
    // Body
    Vtop___024root___eval_triggers__ico(vlSelf);
    __VicoExecute = vlSelfRef.__VicoTriggered.any();
    if (__VicoExecute) {
        Vtop___024root___eval_ico(vlSelf);
    }
    return (__VicoExecute);
}

void Vtop___024root___eval_act(Vtop___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_act\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
}

void Vtop___024root___eval_nba(Vtop___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_nba\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
}

void Vtop___024root___eval_triggers__act(Vtop___024root* vlSelf);

bool Vtop___024root___eval_phase__act(Vtop___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_phase__act\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
    // Init
    VlTriggerVec<0> __VpreTriggered;
    CData/*0:0*/ __VactExecute;
    // Body
    Vtop___024root___eval_triggers__act(vlSelf);
    __VactExecute = vlSelfRef.__VactTriggered.any();
    if (__VactExecute) {
        __VpreTriggered.andNot(vlSelfRef.__VactTriggered, vlSelfRef.__VnbaTriggered);
        vlSelfRef.__VnbaTriggered.thisOr(vlSelfRef.__VactTriggered);
        Vtop___024root___eval_act(vlSelf);
    }
    return (__VactExecute);
}

bool Vtop___024root___eval_phase__nba(Vtop___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_phase__nba\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
    // Init
    CData/*0:0*/ __VnbaExecute;
    // Body
    __VnbaExecute = vlSelfRef.__VnbaTriggered.any();
    if (__VnbaExecute) {
        Vtop___024root___eval_nba(vlSelf);
        vlSelfRef.__VnbaTriggered.clear();
    }
    return (__VnbaExecute);
}

#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__ico(Vtop___024root* vlSelf);
#endif  // VL_DEBUG
#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__nba(Vtop___024root* vlSelf);
#endif  // VL_DEBUG
#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__act(Vtop___024root* vlSelf);
#endif  // VL_DEBUG

void Vtop___024root___eval(Vtop___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
    // Init
    IData/*31:0*/ __VicoIterCount;
    CData/*0:0*/ __VicoContinue;
    IData/*31:0*/ __VnbaIterCount;
    CData/*0:0*/ __VnbaContinue;
    // Body
    __VicoIterCount = 0U;
    vlSelfRef.__VicoFirstIteration = 1U;
    __VicoContinue = 1U;
    while (__VicoContinue) {
        if (VL_UNLIKELY((0x64U < __VicoIterCount))) {
#ifdef VL_DEBUG
            Vtop___024root___dump_triggers__ico(vlSelf);
#endif
            VL_FATAL_MT("/home/loop/Documents/HW/ALU/ALU_RV32I.sv", 1, "", "Input combinational region did not converge.");
        }
        __VicoIterCount = ((IData)(1U) + __VicoIterCount);
        __VicoContinue = 0U;
        if (Vtop___024root___eval_phase__ico(vlSelf)) {
            __VicoContinue = 1U;
        }
        vlSelfRef.__VicoFirstIteration = 0U;
    }
    __VnbaIterCount = 0U;
    __VnbaContinue = 1U;
    while (__VnbaContinue) {
        if (VL_UNLIKELY((0x64U < __VnbaIterCount))) {
#ifdef VL_DEBUG
            Vtop___024root___dump_triggers__nba(vlSelf);
#endif
            VL_FATAL_MT("/home/loop/Documents/HW/ALU/ALU_RV32I.sv", 1, "", "NBA region did not converge.");
        }
        __VnbaIterCount = ((IData)(1U) + __VnbaIterCount);
        __VnbaContinue = 0U;
        vlSelfRef.__VactIterCount = 0U;
        vlSelfRef.__VactContinue = 1U;
        while (vlSelfRef.__VactContinue) {
            if (VL_UNLIKELY((0x64U < vlSelfRef.__VactIterCount))) {
#ifdef VL_DEBUG
                Vtop___024root___dump_triggers__act(vlSelf);
#endif
                VL_FATAL_MT("/home/loop/Documents/HW/ALU/ALU_RV32I.sv", 1, "", "Active region did not converge.");
            }
            vlSelfRef.__VactIterCount = ((IData)(1U) 
                                         + vlSelfRef.__VactIterCount);
            vlSelfRef.__VactContinue = 0U;
            if (Vtop___024root___eval_phase__act(vlSelf)) {
                vlSelfRef.__VactContinue = 1U;
            }
        }
        if (Vtop___024root___eval_phase__nba(vlSelf)) {
            __VnbaContinue = 1U;
        }
    }
}

#ifdef VL_DEBUG
void Vtop___024root___eval_debug_assertions(Vtop___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_debug_assertions\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if (VL_UNLIKELY((vlSelfRef.op & 0xf0U))) {
        Verilated::overWidthError("op");}
    if (VL_UNLIKELY((vlSelfRef.a & 0xf0U))) {
        Verilated::overWidthError("a");}
    if (VL_UNLIKELY((vlSelfRef.b & 0xf0U))) {
        Verilated::overWidthError("b");}
}
#endif  // VL_DEBUG
