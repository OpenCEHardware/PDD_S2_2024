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
    // Body
    vlSelfRef.generic_fifo__DOT__aclk = vlSelfRef.aclk;
    vlSelfRef.generic_fifo__DOT__resetn = vlSelfRef.resetn;
    vlSelfRef.generic_fifo__DOT__data_in[0U] = vlSelfRef.data_in[0U];
    vlSelfRef.generic_fifo__DOT__data_in[1U] = vlSelfRef.data_in[1U];
    vlSelfRef.generic_fifo__DOT__data_in[2U] = vlSelfRef.data_in[2U];
    vlSelfRef.generic_fifo__DOT__push = vlSelfRef.push;
    vlSelfRef.generic_fifo__DOT__pop = vlSelfRef.pop;
    vlSelfRef.rd_ptr = vlSelfRef.generic_fifo__DOT__rd_ptr;
    vlSelfRef.wr_ptr = vlSelfRef.generic_fifo__DOT__wr_ptr;
    vlSelfRef.data_out[0U] = vlSelfRef.generic_fifo__DOT__data_out[0U];
    vlSelfRef.data_out[1U] = vlSelfRef.generic_fifo__DOT__data_out[1U];
    vlSelfRef.data_out[2U] = vlSelfRef.generic_fifo__DOT__data_out[2U];
    vlSelfRef.generic_fifo__DOT__empty = (0U == (IData)(vlSelfRef.generic_fifo__DOT__count));
    vlSelfRef.generic_fifo__DOT__full = (1U & ((IData)(vlSelfRef.generic_fifo__DOT__count) 
                                               >> 1U));
    vlSelfRef.empty = vlSelfRef.generic_fifo__DOT__empty;
    vlSelfRef.full = vlSelfRef.generic_fifo__DOT__full;
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

void Vtop___024root___nba_sequent__TOP__0(Vtop___024root* vlSelf);

void Vtop___024root___eval_nba(Vtop___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_nba\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if ((1ULL & vlSelfRef.__VnbaTriggered.word(0U))) {
        Vtop___024root___nba_sequent__TOP__0(vlSelf);
    }
}

VL_INLINE_OPT void Vtop___024root___nba_sequent__TOP__0(Vtop___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___nba_sequent__TOP__0\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
    // Init
    CData/*0:0*/ __Vdly__generic_fifo__DOT__rd_ptr;
    __Vdly__generic_fifo__DOT__rd_ptr = 0;
    CData/*0:0*/ __Vdly__generic_fifo__DOT__wr_ptr;
    __Vdly__generic_fifo__DOT__wr_ptr = 0;
    VlWide<3>/*83:0*/ __VdlyVal__generic_fifo__DOT__mem__v0;
    VL_ZERO_W(84, __VdlyVal__generic_fifo__DOT__mem__v0);
    CData/*0:0*/ __VdlyDim0__generic_fifo__DOT__mem__v0;
    __VdlyDim0__generic_fifo__DOT__mem__v0 = 0;
    CData/*1:0*/ __Vdly__generic_fifo__DOT__count;
    __Vdly__generic_fifo__DOT__count = 0;
    CData/*0:0*/ __VdlySet__generic_fifo__DOT__mem__v0;
    __VdlySet__generic_fifo__DOT__mem__v0 = 0;
    CData/*0:0*/ __VdlySet__generic_fifo__DOT__mem__v1;
    __VdlySet__generic_fifo__DOT__mem__v1 = 0;
    // Body
    __Vdly__generic_fifo__DOT__rd_ptr = vlSelfRef.generic_fifo__DOT__rd_ptr;
    __Vdly__generic_fifo__DOT__wr_ptr = vlSelfRef.generic_fifo__DOT__wr_ptr;
    __VdlySet__generic_fifo__DOT__mem__v0 = 0U;
    __VdlySet__generic_fifo__DOT__mem__v1 = 0U;
    __Vdly__generic_fifo__DOT__count = vlSelfRef.generic_fifo__DOT__count;
    if ((1U & (~ (IData)(vlSelfRef.resetn)))) {
        vlSelfRef.generic_fifo__DOT__unnamedblk1__DOT__i = 1U;
    }
    if (vlSelfRef.resetn) {
        if (((~ (IData)(vlSelfRef.generic_fifo__DOT__full)) 
             & (IData)(vlSelfRef.push))) {
            __Vdly__generic_fifo__DOT__wr_ptr = (1U 
                                                 & ((IData)(1U) 
                                                    + (IData)(vlSelfRef.generic_fifo__DOT__wr_ptr)));
            __VdlyVal__generic_fifo__DOT__mem__v0[0U] 
                = vlSelfRef.data_in[0U];
            __VdlyVal__generic_fifo__DOT__mem__v0[1U] 
                = vlSelfRef.data_in[1U];
            __VdlyVal__generic_fifo__DOT__mem__v0[2U] 
                = vlSelfRef.data_in[2U];
            __VdlyDim0__generic_fifo__DOT__mem__v0 
                = vlSelfRef.generic_fifo__DOT__wr_ptr;
            __VdlySet__generic_fifo__DOT__mem__v0 = 1U;
            __Vdly__generic_fifo__DOT__count = (3U 
                                                & ((IData)(1U) 
                                                   + (IData)(vlSelfRef.generic_fifo__DOT__count)));
        }
        if (((~ (IData)(vlSelfRef.generic_fifo__DOT__empty)) 
             & (IData)(vlSelfRef.pop))) {
            __Vdly__generic_fifo__DOT__count = (3U 
                                                & ((IData)(vlSelfRef.generic_fifo__DOT__count) 
                                                   - (IData)(1U)));
            __Vdly__generic_fifo__DOT__rd_ptr = (1U 
                                                 & ((IData)(1U) 
                                                    + (IData)(vlSelfRef.generic_fifo__DOT__rd_ptr)));
            vlSelfRef.generic_fifo__DOT__data_out[0U] 
                = vlSelfRef.generic_fifo__DOT__mem[vlSelfRef.generic_fifo__DOT__rd_ptr][0U];
            vlSelfRef.generic_fifo__DOT__data_out[1U] 
                = vlSelfRef.generic_fifo__DOT__mem[vlSelfRef.generic_fifo__DOT__rd_ptr][1U];
            vlSelfRef.generic_fifo__DOT__data_out[2U] 
                = vlSelfRef.generic_fifo__DOT__mem[vlSelfRef.generic_fifo__DOT__rd_ptr][2U];
        }
    } else {
        __Vdly__generic_fifo__DOT__wr_ptr = 0U;
        __VdlySet__generic_fifo__DOT__mem__v1 = 1U;
        __Vdly__generic_fifo__DOT__count = 0U;
        vlSelfRef.generic_fifo__DOT__mem[0U][2U] = 
            (0xff0ffU & vlSelfRef.generic_fifo__DOT__mem
             [0U][2U]);
        __Vdly__generic_fifo__DOT__rd_ptr = 0U;
        vlSelfRef.generic_fifo__DOT__mem[0U][0U] = 
            (0xffU & vlSelfRef.generic_fifo__DOT__mem
             [0U][0U]);
        vlSelfRef.generic_fifo__DOT__mem[0U][1U] = 0xffffff00U;
        vlSelfRef.generic_fifo__DOT__mem[0U][2U] = 
            (0xffU | (0xfff00U & vlSelfRef.generic_fifo__DOT__mem
                      [0U][2U]));
        vlSelfRef.generic_fifo__DOT__mem[0U][0U] = 
            (0xffffff0fU & vlSelfRef.generic_fifo__DOT__mem
             [0U][0U]);
        vlSelfRef.generic_fifo__DOT__mem[0U][0U] = 
            (1U | (0xfffffff0U & vlSelfRef.generic_fifo__DOT__mem
                   [0U][0U]));
        vlSelfRef.generic_fifo__DOT__data_out[0U] = 
            vlSelfRef.generic_fifo__DOT__mem[0U][0U];
        vlSelfRef.generic_fifo__DOT__data_out[1U] = 
            vlSelfRef.generic_fifo__DOT__mem[0U][1U];
        vlSelfRef.generic_fifo__DOT__data_out[2U] = 
            vlSelfRef.generic_fifo__DOT__mem[0U][2U];
    }
    vlSelfRef.generic_fifo__DOT__wr_ptr = __Vdly__generic_fifo__DOT__wr_ptr;
    vlSelfRef.generic_fifo__DOT__count = __Vdly__generic_fifo__DOT__count;
    vlSelfRef.generic_fifo__DOT__rd_ptr = __Vdly__generic_fifo__DOT__rd_ptr;
    if (__VdlySet__generic_fifo__DOT__mem__v0) {
        vlSelfRef.generic_fifo__DOT__mem[__VdlyDim0__generic_fifo__DOT__mem__v0][0U] 
            = __VdlyVal__generic_fifo__DOT__mem__v0[0U];
        vlSelfRef.generic_fifo__DOT__mem[__VdlyDim0__generic_fifo__DOT__mem__v0][1U] 
            = __VdlyVal__generic_fifo__DOT__mem__v0[1U];
        vlSelfRef.generic_fifo__DOT__mem[__VdlyDim0__generic_fifo__DOT__mem__v0][2U] 
            = __VdlyVal__generic_fifo__DOT__mem__v0[2U];
    }
    if (__VdlySet__generic_fifo__DOT__mem__v1) {
        vlSelfRef.generic_fifo__DOT__mem[0U][2U] = 
            (0xfffU & vlSelfRef.generic_fifo__DOT__mem
             [0U][2U]);
    }
    vlSelfRef.wr_ptr = vlSelfRef.generic_fifo__DOT__wr_ptr;
    vlSelfRef.generic_fifo__DOT__empty = (0U == (IData)(vlSelfRef.generic_fifo__DOT__count));
    vlSelfRef.generic_fifo__DOT__full = (1U & ((IData)(vlSelfRef.generic_fifo__DOT__count) 
                                               >> 1U));
    vlSelfRef.rd_ptr = vlSelfRef.generic_fifo__DOT__rd_ptr;
    vlSelfRef.data_out[0U] = vlSelfRef.generic_fifo__DOT__data_out[0U];
    vlSelfRef.data_out[1U] = vlSelfRef.generic_fifo__DOT__data_out[1U];
    vlSelfRef.data_out[2U] = vlSelfRef.generic_fifo__DOT__data_out[2U];
    vlSelfRef.empty = vlSelfRef.generic_fifo__DOT__empty;
    vlSelfRef.full = vlSelfRef.generic_fifo__DOT__full;
}

void Vtop___024root___eval_triggers__act(Vtop___024root* vlSelf);

bool Vtop___024root___eval_phase__act(Vtop___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_phase__act\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
    // Init
    VlTriggerVec<1> __VpreTriggered;
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
            VL_FATAL_MT("/mnt/d/D/TEC/2024/S2/Proyecto_de_diseno/Pruebas/modules/generic_fifo.sv", 4, "", "Input combinational region did not converge.");
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
            VL_FATAL_MT("/mnt/d/D/TEC/2024/S2/Proyecto_de_diseno/Pruebas/modules/generic_fifo.sv", 4, "", "NBA region did not converge.");
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
                VL_FATAL_MT("/mnt/d/D/TEC/2024/S2/Proyecto_de_diseno/Pruebas/modules/generic_fifo.sv", 4, "", "Active region did not converge.");
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
    if (VL_UNLIKELY((vlSelfRef.aclk & 0xfeU))) {
        Verilated::overWidthError("aclk");}
    if (VL_UNLIKELY((vlSelfRef.resetn & 0xfeU))) {
        Verilated::overWidthError("resetn");}
    if (VL_UNLIKELY((vlSelfRef.push & 0xfeU))) {
        Verilated::overWidthError("push");}
    if (VL_UNLIKELY((vlSelfRef.pop & 0xfeU))) {
        Verilated::overWidthError("pop");}
}
#endif  // VL_DEBUG
