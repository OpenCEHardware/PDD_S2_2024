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

- **Python 3.x**
- **PyYAML**: Install by running `pip install pyyaml`
- **Jinja**: Install by running `pip install jinja2`
- If you are running the tool on **Windows**, ensure that **WSL (Windows Subsystem for Linux)** is installed.

In **WSL**, install:

- **cocotb**: Run `pip install cocotb`
- **Verilator** and/or **Questa**, depending on your needs.
- A functional **C++** compiler for use with Verilator.


#### For windows
##### Setting script policy in PowerShell
```
Set-ExecutionPolicy -ExecutionPolicy Bypass
```




#### For Ubuntu



##### Install cocotb (1.9.1 or 1.9.0)
`pip3 install cocotb`

###### Verify Installation
`pip3 show cocotb`

###### Check if cocotb can be called
`cocotb-config --version`

###### If not working, add to PATH. Edit .bashrc with nano:
`nano ~/.bashrc`

###### Add the following line:
export PATH=$PATH:/home/<user>/.local/bin

###### Apply changes for .bashrc
`source ~/.bashrc`


##### Install Verilator (only 5.022 or higher)
###### Install dependencies
`sudo apt-get install git make autoconf g++ flex bison libfl-dev libgoogle-perftools-dev numactl perl python3`

###### Install help2man
`sudo apt-get install help2man`

###### Clone Verilator
```bash
git clone https://github.com/verilator/verilator
cd verilator
git checkout v5.028
```
###### Configure and install Verilator
```bash
autoconf
./configure
make -j$(nproc)
make test
sudo make install
```

###### Verify Installation
ls /usr/local/bin/verilator

###### This will place it here:
/usr/local/bin/verilator

###### However, when calling it, it looks for it here:
/usr/bin/verilator

###### Add to PATH. Add the next line to .bashrc and then apply changes:
export PATH=$PATH:/usr/local/bin

###### Now verilator --version should work and show something like:
Verilator 5.028 2024-08-21 rev v5.028




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