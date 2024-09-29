// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Symbol table implementation internals

#include "Vtop__pch.h"
#include "Vtop.h"
#include "Vtop___024root.h"

// FUNCTIONS
Vtop__Syms::~Vtop__Syms()
{

    // Tear down scope hierarchy
    __Vhier.remove(0, &__Vscope_ALU_RV32I);
    __Vhier.remove(&__Vscope_ALU_RV32I, &__Vscope_ALU_RV32I__abs);
    __Vhier.remove(&__Vscope_ALU_RV32I, &__Vscope_ALU_RV32I__add_sub);
    __Vhier.remove(&__Vscope_ALU_RV32I, &__Vscope_ALU_RV32I__mux);
    __Vhier.remove(&__Vscope_ALU_RV32I, &__Vscope_ALU_RV32I__slt);
    __Vhier.remove(&__Vscope_ALU_RV32I__abs, &__Vscope_ALU_RV32I__abs__add);
    __Vhier.remove(&__Vscope_ALU_RV32I__abs, &__Vscope_ALU_RV32I__abs__mux);
    __Vhier.remove(&__Vscope_ALU_RV32I__add_sub, &__Vscope_ALU_RV32I__add_sub__a1);
    __Vhier.remove(&__Vscope_ALU_RV32I__add_sub, &__Vscope_ALU_RV32I__add_sub__adder);
    __Vhier.remove(&__Vscope_ALU_RV32I__slt, &__Vscope_ALU_RV32I__slt__adder);

}

Vtop__Syms::Vtop__Syms(VerilatedContext* contextp, const char* namep, Vtop* modelp)
    : VerilatedSyms{contextp}
    // Setup internal state of the Syms class
    , __Vm_modelp{modelp}
    // Setup module instances
    , TOP{this, namep}
{
        // Check resources
        Verilated::stackCheck(97);
    // Configure time unit / time precision
    _vm_contextp__->timeunit(-8);
    _vm_contextp__->timeprecision(-11);
    // Setup each module's pointers to their submodules
    // Setup each module's pointer back to symbol table (for public functions)
    TOP.__Vconfigure(true);
    // Setup scopes
    __Vscope_ALU_RV32I.configure(this, name(), "ALU_RV32I", "ALU_RV32I", -8, VerilatedScope::SCOPE_MODULE);
    __Vscope_ALU_RV32I__abs.configure(this, name(), "ALU_RV32I.abs", "abs", -8, VerilatedScope::SCOPE_MODULE);
    __Vscope_ALU_RV32I__abs__add.configure(this, name(), "ALU_RV32I.abs.add", "add", -8, VerilatedScope::SCOPE_MODULE);
    __Vscope_ALU_RV32I__abs__mux.configure(this, name(), "ALU_RV32I.abs.mux", "mux", -8, VerilatedScope::SCOPE_MODULE);
    __Vscope_ALU_RV32I__add_sub.configure(this, name(), "ALU_RV32I.add_sub", "add_sub", -8, VerilatedScope::SCOPE_MODULE);
    __Vscope_ALU_RV32I__add_sub__a1.configure(this, name(), "ALU_RV32I.add_sub.a1", "a1", -8, VerilatedScope::SCOPE_MODULE);
    __Vscope_ALU_RV32I__add_sub__adder.configure(this, name(), "ALU_RV32I.add_sub.adder", "adder", -8, VerilatedScope::SCOPE_MODULE);
    __Vscope_ALU_RV32I__mux.configure(this, name(), "ALU_RV32I.mux", "mux", -8, VerilatedScope::SCOPE_MODULE);
    __Vscope_ALU_RV32I__slt.configure(this, name(), "ALU_RV32I.slt", "slt", -8, VerilatedScope::SCOPE_MODULE);
    __Vscope_ALU_RV32I__slt__adder.configure(this, name(), "ALU_RV32I.slt.adder", "adder", -8, VerilatedScope::SCOPE_MODULE);
    __Vscope_TOP.configure(this, name(), "TOP", "TOP", 0, VerilatedScope::SCOPE_OTHER);

    // Set up scope hierarchy
    __Vhier.add(0, &__Vscope_ALU_RV32I);
    __Vhier.add(&__Vscope_ALU_RV32I, &__Vscope_ALU_RV32I__abs);
    __Vhier.add(&__Vscope_ALU_RV32I, &__Vscope_ALU_RV32I__add_sub);
    __Vhier.add(&__Vscope_ALU_RV32I, &__Vscope_ALU_RV32I__mux);
    __Vhier.add(&__Vscope_ALU_RV32I, &__Vscope_ALU_RV32I__slt);
    __Vhier.add(&__Vscope_ALU_RV32I__abs, &__Vscope_ALU_RV32I__abs__add);
    __Vhier.add(&__Vscope_ALU_RV32I__abs, &__Vscope_ALU_RV32I__abs__mux);
    __Vhier.add(&__Vscope_ALU_RV32I__add_sub, &__Vscope_ALU_RV32I__add_sub__a1);
    __Vhier.add(&__Vscope_ALU_RV32I__add_sub, &__Vscope_ALU_RV32I__add_sub__adder);
    __Vhier.add(&__Vscope_ALU_RV32I__slt, &__Vscope_ALU_RV32I__slt__adder);

    // Setup export functions
    for (int __Vfinal = 0; __Vfinal < 2; ++__Vfinal) {
        __Vscope_ALU_RV32I.varInsert(__Vfinal,"N", const_cast<void*>(static_cast<const void*>(&(TOP.ALU_RV32I__DOT__N))), true, VLVT_UINT32,VLVD_NODIR|VLVF_PUB_RW,1 ,31,0);
        __Vscope_ALU_RV32I.varInsert(__Vfinal,"a", &(TOP.ALU_RV32I__DOT__a), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I.varInsert(__Vfinal,"a_signed_for_shift_right_arithmetic", &(TOP.ALU_RV32I__DOT__a_signed_for_shift_right_arithmetic), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I.varInsert(__Vfinal,"abs_o", &(TOP.ALU_RV32I__DOT__abs_o), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I.varInsert(__Vfinal,"add_sub_o", &(TOP.ALU_RV32I__DOT__add_sub_o), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I.varInsert(__Vfinal,"b", &(TOP.ALU_RV32I__DOT__b), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I.varInsert(__Vfinal,"o", &(TOP.ALU_RV32I__DOT__o), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I.varInsert(__Vfinal,"op", &(TOP.ALU_RV32I__DOT__op), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I.varInsert(__Vfinal,"slt_o", &(TOP.ALU_RV32I__DOT__slt_o), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I__abs.varInsert(__Vfinal,"A", &(TOP.ALU_RV32I__DOT__abs__DOT__A), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I__abs.varInsert(__Vfinal,"N", const_cast<void*>(static_cast<const void*>(&(TOP.ALU_RV32I__DOT__abs__DOT__N))), true, VLVT_UINT32,VLVD_NODIR|VLVF_PUB_RW,1 ,31,0);
        __Vscope_ALU_RV32I__abs.varInsert(__Vfinal,"abs_A", &(TOP.ALU_RV32I__DOT__abs__DOT__abs_A), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I__abs.varInsert(__Vfinal,"adder_o", &(TOP.ALU_RV32I__DOT__abs__DOT__adder_o), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I__abs__add.varInsert(__Vfinal,"A", &(TOP.ALU_RV32I__DOT__abs__DOT__add__DOT__A), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I__abs__add.varInsert(__Vfinal,"B", &(TOP.ALU_RV32I__DOT__abs__DOT__add__DOT__B), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I__abs__add.varInsert(__Vfinal,"N", const_cast<void*>(static_cast<const void*>(&(TOP.ALU_RV32I__DOT__abs__DOT__add__DOT__N))), true, VLVT_UINT32,VLVD_NODIR|VLVF_PUB_RW,1 ,31,0);
        __Vscope_ALU_RV32I__abs__add.varInsert(__Vfinal,"O", &(TOP.ALU_RV32I__DOT__abs__DOT__add__DOT__O), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I__abs__add.varInsert(__Vfinal,"ci", &(TOP.ALU_RV32I__DOT__abs__DOT__add__DOT__ci), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0);
        __Vscope_ALU_RV32I__abs__mux.varInsert(__Vfinal,"M", const_cast<void*>(static_cast<const void*>(&(TOP.ALU_RV32I__DOT__abs__DOT__mux__DOT__M))), true, VLVT_UINT32,VLVD_NODIR|VLVF_PUB_RW,1 ,31,0);
        __Vscope_ALU_RV32I__abs__mux.varInsert(__Vfinal,"N", const_cast<void*>(static_cast<const void*>(&(TOP.ALU_RV32I__DOT__abs__DOT__mux__DOT__N))), true, VLVT_UINT32,VLVD_NODIR|VLVF_PUB_RW,1 ,31,0);
        __Vscope_ALU_RV32I__abs__mux.varInsert(__Vfinal,"channel_out", &(TOP.ALU_RV32I__DOT__abs__DOT__mux__DOT__channel_out), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I__abs__mux.varInsert(__Vfinal,"channels", &(TOP.ALU_RV32I__DOT__abs__DOT__mux__DOT__channels), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1, 7,0);
        __Vscope_ALU_RV32I__abs__mux.varInsert(__Vfinal,"select", &(TOP.ALU_RV32I__DOT__abs__DOT__mux__DOT__select), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,0,0);
        __Vscope_ALU_RV32I__add_sub.varInsert(__Vfinal,"N", const_cast<void*>(static_cast<const void*>(&(TOP.ALU_RV32I__DOT__add_sub__DOT__N))), true, VLVT_UINT32,VLVD_NODIR|VLVF_PUB_RW,1 ,31,0);
        __Vscope_ALU_RV32I__add_sub.varInsert(__Vfinal,"a", &(TOP.ALU_RV32I__DOT__add_sub__DOT__a), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I__add_sub.varInsert(__Vfinal,"b", &(TOP.ALU_RV32I__DOT__add_sub__DOT__b), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I__add_sub.varInsert(__Vfinal,"b_a1", &(TOP.ALU_RV32I__DOT__add_sub__DOT__b_a1), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I__add_sub.varInsert(__Vfinal,"o", &(TOP.ALU_RV32I__DOT__add_sub__DOT__o), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I__add_sub.varInsert(__Vfinal,"op", &(TOP.ALU_RV32I__DOT__add_sub__DOT__op), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0);
        __Vscope_ALU_RV32I__add_sub__a1.varInsert(__Vfinal,"N", const_cast<void*>(static_cast<const void*>(&(TOP.ALU_RV32I__DOT__add_sub__DOT__a1__DOT__N))), true, VLVT_UINT32,VLVD_NODIR|VLVF_PUB_RW,1 ,31,0);
        __Vscope_ALU_RV32I__add_sub__a1.varInsert(__Vfinal,"a", &(TOP.ALU_RV32I__DOT__add_sub__DOT__a1__DOT__a), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I__add_sub__a1.varInsert(__Vfinal,"a1", &(TOP.ALU_RV32I__DOT__add_sub__DOT__a1__DOT__a1), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I__add_sub__a1.varInsert(__Vfinal,"on", &(TOP.ALU_RV32I__DOT__add_sub__DOT__a1__DOT__on), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0);
        __Vscope_ALU_RV32I__add_sub__adder.varInsert(__Vfinal,"A", &(TOP.ALU_RV32I__DOT__add_sub__DOT__adder__DOT__A), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I__add_sub__adder.varInsert(__Vfinal,"B", &(TOP.ALU_RV32I__DOT__add_sub__DOT__adder__DOT__B), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I__add_sub__adder.varInsert(__Vfinal,"N", const_cast<void*>(static_cast<const void*>(&(TOP.ALU_RV32I__DOT__add_sub__DOT__adder__DOT__N))), true, VLVT_UINT32,VLVD_NODIR|VLVF_PUB_RW,1 ,31,0);
        __Vscope_ALU_RV32I__add_sub__adder.varInsert(__Vfinal,"O", &(TOP.ALU_RV32I__DOT__add_sub__DOT__adder__DOT__O), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I__add_sub__adder.varInsert(__Vfinal,"ci", &(TOP.ALU_RV32I__DOT__add_sub__DOT__adder__DOT__ci), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0);
        __Vscope_ALU_RV32I__mux.varInsert(__Vfinal,"M", const_cast<void*>(static_cast<const void*>(&(TOP.ALU_RV32I__DOT__mux__DOT__M))), true, VLVT_UINT32,VLVD_NODIR|VLVF_PUB_RW,1 ,31,0);
        __Vscope_ALU_RV32I__mux.varInsert(__Vfinal,"N", const_cast<void*>(static_cast<const void*>(&(TOP.ALU_RV32I__DOT__mux__DOT__N))), true, VLVT_UINT32,VLVD_NODIR|VLVF_PUB_RW,1 ,31,0);
        __Vscope_ALU_RV32I__mux.varInsert(__Vfinal,"channel_out", &(TOP.ALU_RV32I__DOT__mux__DOT__channel_out), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I__mux.varInsert(__Vfinal,"channels", &(TOP.ALU_RV32I__DOT__mux__DOT__channels), false, VLVT_UINT64,VLVD_NODIR|VLVF_PUB_RW,1, 63,0);
        __Vscope_ALU_RV32I__mux.varInsert(__Vfinal,"select", &(TOP.ALU_RV32I__DOT__mux__DOT__select), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I__slt.varInsert(__Vfinal,"N", const_cast<void*>(static_cast<const void*>(&(TOP.ALU_RV32I__DOT__slt__DOT__N))), true, VLVT_UINT32,VLVD_NODIR|VLVF_PUB_RW,1 ,31,0);
        __Vscope_ALU_RV32I__slt.varInsert(__Vfinal,"a", &(TOP.ALU_RV32I__DOT__slt__DOT__a), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I__slt.varInsert(__Vfinal,"adder_o", &(TOP.ALU_RV32I__DOT__slt__DOT__adder_o), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I__slt.varInsert(__Vfinal,"b", &(TOP.ALU_RV32I__DOT__slt__DOT__b), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I__slt.varInsert(__Vfinal,"co", &(TOP.ALU_RV32I__DOT__slt__DOT__co), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0);
        __Vscope_ALU_RV32I__slt.varInsert(__Vfinal,"o", &(TOP.ALU_RV32I__DOT__slt__DOT__o), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I__slt.varInsert(__Vfinal,"o_aux", &(TOP.ALU_RV32I__DOT__slt__DOT__o_aux), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0);
        __Vscope_ALU_RV32I__slt.varInsert(__Vfinal,"unsigned_", &(TOP.ALU_RV32I__DOT__slt__DOT__unsigned_), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0);
        __Vscope_ALU_RV32I__slt__adder.varInsert(__Vfinal,"A", &(TOP.ALU_RV32I__DOT__slt__DOT__adder__DOT__A), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I__slt__adder.varInsert(__Vfinal,"B", &(TOP.ALU_RV32I__DOT__slt__DOT__adder__DOT__B), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I__slt__adder.varInsert(__Vfinal,"N", const_cast<void*>(static_cast<const void*>(&(TOP.ALU_RV32I__DOT__slt__DOT__adder__DOT__N))), true, VLVT_UINT32,VLVD_NODIR|VLVF_PUB_RW,1 ,31,0);
        __Vscope_ALU_RV32I__slt__adder.varInsert(__Vfinal,"O", &(TOP.ALU_RV32I__DOT__slt__DOT__adder__DOT__O), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ALU_RV32I__slt__adder.varInsert(__Vfinal,"ci", &(TOP.ALU_RV32I__DOT__slt__DOT__adder__DOT__ci), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0);
        __Vscope_ALU_RV32I__slt__adder.varInsert(__Vfinal,"co", &(TOP.ALU_RV32I__DOT__slt__DOT__adder__DOT__co), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0);
        __Vscope_TOP.varInsert(__Vfinal,"a", &(TOP.a), false, VLVT_UINT8,VLVD_IN|VLVF_PUB_RW,1 ,3,0);
        __Vscope_TOP.varInsert(__Vfinal,"b", &(TOP.b), false, VLVT_UINT8,VLVD_IN|VLVF_PUB_RW,1 ,3,0);
        __Vscope_TOP.varInsert(__Vfinal,"o", &(TOP.o), false, VLVT_UINT8,VLVD_OUT|VLVF_PUB_RW,1 ,3,0);
        __Vscope_TOP.varInsert(__Vfinal,"op", &(TOP.op), false, VLVT_UINT8,VLVD_IN|VLVF_PUB_RW,1 ,3,0);
    }
}
