# Autococo (Automatic cocotb based hardware testbench generator tool)

## Overview

This tool automates the creation of testbenches for hardware modules written in SystemVerilog (`.sv`), using cocotb as the test framework. It supports running simulations using **Verilator** or **Questa**, generating the necessary cocotb template and Makefile. The tool simplifies the testing workflow by automatically configuring the simulator, handling testbench creation, and managing file paths.

## Features

- **Automatic Testbench Creation**: Generates cocotb testbenches for SystemVerilog files based on metadata provided in a YAML file.
- **Simulator Integration**: Supports both **Verilator** and **Questa** simulators for running the generated testbenches.
- **Customizable Inputs and Outputs**: You can specify the inputs, outputs, clocks, and resets of the DUT (Device Under Test) through the YAML configuration.
- **Makefile Generation**: Creates a Makefile that runs the cocotb testbench with the selected simulator.
- **Cross-Platform Support**: Works on both Linux (Ubuntu) and Windows environments.

## Usage

### 1. Prerequisites

Make sure the following dependencies are installed:

- Python 3.x
- cocotb
- Verilator or Questa (depending on your needs)
- A working C++ compiler for Verilator
- Ensure that [WSL (Windows Subsystem for Linux)] is installed if you are running the tool on Windows.

### 2. Installation

Clone the repository and install the required Python packages.

```bash
git clone https://github.com/MajinLoop/PDD_S2_2024.git
cd <your-repo-directory>
pip install -r requirements.txt



# PDD_S2_2024

## Uso
### 1. Abrir powershell en la carpeta src
### 2. ejecutar el comando python .\cmd_controller.py ruta\al\yaml_file
### 3. Esto generará una carpeta "test" en la ubicación especificada en el yaml, concretamente dada por la llave "output_dir"