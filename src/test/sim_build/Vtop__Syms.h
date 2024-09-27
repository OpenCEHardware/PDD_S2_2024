// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Symbol table internal header
//
// Internal details; most calling programs do not need this header,
// unless using verilator public meta comments.

#ifndef VERILATED_VTOP__SYMS_H_
#define VERILATED_VTOP__SYMS_H_  // guard

#include "verilated.h"

// INCLUDE MODEL CLASS

#include "Vtop.h"

// INCLUDE MODULE CLASSES
#include "Vtop___024root.h"

// DPI TYPES for DPI Export callbacks (Internal use)

// SYMS CLASS (contains all model state)
class alignas(VL_CACHE_LINE_BYTES)Vtop__Syms final : public VerilatedSyms {
  public:
    // INTERNAL STATE
    Vtop* const __Vm_modelp;
    VlDeleter __Vm_deleter;
    bool __Vm_didInit = false;

    // MODULE INSTANCE STATE
    Vtop___024root                 TOP;

    // SCOPE NAMES
    VerilatedScope __Vscope_ALU_RV32I;
    VerilatedScope __Vscope_ALU_RV32I__abs;
    VerilatedScope __Vscope_ALU_RV32I__abs__add;
    VerilatedScope __Vscope_ALU_RV32I__abs__mux;
    VerilatedScope __Vscope_ALU_RV32I__add_sub;
    VerilatedScope __Vscope_ALU_RV32I__add_sub__a1;
    VerilatedScope __Vscope_ALU_RV32I__add_sub__adder;
    VerilatedScope __Vscope_ALU_RV32I__mux;
    VerilatedScope __Vscope_ALU_RV32I__slt;
    VerilatedScope __Vscope_ALU_RV32I__slt__adder;
    VerilatedScope __Vscope_TOP;

    // SCOPE HIERARCHY
    VerilatedHierarchy __Vhier;

    // CONSTRUCTORS
    Vtop__Syms(VerilatedContext* contextp, const char* namep, Vtop* modelp);
    ~Vtop__Syms();

    // METHODS
    const char* name() { return TOP.name(); }
};

#endif  // guard
