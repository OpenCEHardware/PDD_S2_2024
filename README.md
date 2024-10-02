# Autococo (Automatic cocotb based hardware testbench generator tool)


## Overview

This tool automates the creation of testbenches for hardware modules written in SystemVerilog (`.sv`), using cocotb as the test framework. It supports running simulations using **Verilator** or **Questa**, generating the necessary cocotb template and Makefile. The tool simplifies the testing workflow by automatically configuring the simulator, handling testbench creation, and managing file paths.


## Features

- **Automatic Testbench Creation**: Generates cocotb testbenches for SystemVerilog files based on metadata provided in a YAML file.
- **Simulator Integration**: Supports both **Verilator** and **Questa** simulators for running the generated testbenches.
- **Customizable Inputs and Outputs**: You can specify the inputs, outputs, clocks, and resets of the DUT (Device Under Test) through the YAML configuration.
- **Makefile Generation**: Creates a Makefile that runs the cocotb testbench with the selected simulator.
- **Cross-Platform Support**: Works on both Linux (Ubuntu) and Windows environments.


## Setup

### 1. Prerequisites

Make sure the following dependencies are installed:

- Python 3.x
- cocotb
- Verilator and/or Questa (depending on your needs)
- A working C++ compiler for Verilator
- Ensure that [WSL (Windows Subsystem for Linux)] is installed if you are running the tool on Windows.
- Set script policy to 'Bypass'


#### For windows
##### Setting script policy in PowerShell
```
Set-ExecutionPolicy -ExecutionPolicy Bypass
```

##### For Questa Intel FPGA Starter Edition used in Windows WSL
Make sure your WSL mac address is always the same that the one in the license.dat. For this set the variable 'wantmac' in /root/.bashrc by adding.

```
wantmac=xx:xx:xx:xx:xx:xx
mac=$(ip link show eth0 | awk '/ether/ {print $2}')
if [[ $mac !=  $wantmac ]]; then
    sudo ip link set dev eth0 down
    sudo ip link set dev eth0 address $wantmac
    sudo ip link set dev eth0 up
fi
```


### 2. Installation

Clone the repository and install the required Python packages.

```bash
git clone https://github.com/MajinLoop/PDD_S2_2024.git
cd <your-repo-directory>
pip install -r requirements.txt
```


## Usage

1. Open PowerShell in the `src` directory.
2. Execute the command: `python .\cmd_controller.py path\to\yaml_file`.
3. This will generate a folder named "test" in the location specified in the YAML file, indicated by the key "output_dir".
4. The flag `-c` compiles the code for the current sim.
5. The flag `-r` runs the current template.


## Notes

In verilator, input values not defined will be assumed as `0`.
In Questa Intel FPGA Starter Edition, input values must be explicitly defined; otherwise, they will be assumed as `x`