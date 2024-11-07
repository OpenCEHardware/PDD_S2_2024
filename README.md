# Autococo: Automatic cocotb-based Hardware Testbench Generator Tool

## Overview
Autococo streamlines the testing of hardware modules written in SystemVerilog (`.sv`) by automating the creation of cocotb-based testbenches. Supporting **Verilator** and **Questa**, this tool generates the necessary cocotb template and Makefile, configures the simulator, and manages file paths. Autococo simplifies testbench setup, enabling seamless simulation and testing.

## Features
- **Automatic Testbench Creation**: Generates cocotb testbenches based on metadata from a YAML file.
- **Simulator Compatibility**: Supports **Verilator** and **Questa** simulators.
- **Customizable Interface**: Specify DUT inputs, outputs, clocks, and resets via YAML.
- **Makefile Generation**: Automatically creates a Makefile for running cocotb testbenches.
- **Cross-Platform Support**: Compatible with both Linux (Ubuntu) and Windows.

## Setup

### 1. Prerequisites
Ensure the following dependencies are installed:

#### Common OS Requirements
- **Python 3.x**
- **PyYAML**: Install with `pip install pyyaml`
- **Jinja2**: Install with `pip install jinja2`

#### Windows Requirements
- **WSL (Windows Subsystem for Linux)**
- **PowerShell Execution Policy**: Change Execution Policy to `bypass` with: `Set-ExecutionPolicy -ExecutionPolicy Bypass`

#### Ubuntu/WSL Requirements
1. **Install cocotb**: 
   ```bash
   pip3 install cocotb
   ```
2. **Verify Installation**:
   ```bash
   pip3 show cocotb
   cocotb-config --version
   ```
   If `cocotb-config` is not found, update the PATH in `.bashrc`:
   ```bash
   nano ~/.bashrc
   export PATH=$PATH:/home/"user"/.local/bin
   source ~/.bashrc
   ```
   
3. **Install Verilator (5.022 or higher)**:
   ```bash
   sudo apt-get install git make autoconf g++ flex bison libfl-dev libgoogle-perftools-dev numactl perl python3 help2man
   git clone https://github.com/verilator/verilator
   cd verilator
   git checkout v5.028
   autoconf
   ./configure
   make -j$(nproc)
   make test
   sudo make install
   ```

4. **Update PATH**:
   ```bash
   export PATH=$PATH:/usr/local/bin
   source ~/.bashrc
   verilator --version
   ```

#### Questa Intel FPGA Starter Edition Setup on WSL
To ensure a stable MAC address, set the `wantmac` variable in `.bashrc`:
```bash
wantmac=xx:xx:xx:xx:xx:xx
mac=$(ip link show eth0 | awk '/ether/ {print $2}')
if [[ $mac != $wantmac ]]; then
    sudo ip link set dev eth0 down
    sudo ip link set dev eth0 address $wantmac
    sudo ip link set dev eth0 up
fi
```

#### Profiling Setup
Install `graphviz` for profiling visualizations:
```bash
pip install gprof2dot
apt-get install python3 graphviz
```

### 2. Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/MajinLoop/PDD_S2_2024.git
cd PDD_S2_2024/src
```

## Usage

To use this tool, adjust the YAML configuration file to specify details about your hardware module and desired test environment. Below is a description of the main YAML keys and instructions on how to configure them to customize the process:

### 1. **output_dir**
   - Defines the directory where all output files, including the testbench and Makefile, will be generated.
   - **Example**: `output_dir: out`

### 2. **template_type**
   - Select the type of test architecture. Use `'simple'` for a direct assertion-based test or `'structured'` for a more comprehensive architecture that includes components like scoreboard, checker, and monitor.
   - **Example**: `template_type: structured`

### 3. **Selecting files**
   - Specify the Verilog files and include directories needed by the simulator:
      - **verilog_sources**: Load SystemVerilog source files.
      - **verilog_sources_and_include_dirs**: Load SystemVerilog header files.
   - **Example**:
   ```yaml
   - verilog_sources:
      - specific_files:
         - /path/to/file_1.sv
         - /path/to/file_2.sv
         - /path/to/file_n.sv

      - load_all_from:
         - /path/to/directory_1
         - /path/to/directory_2
         - /path/to/directory_n
   # This feature 
   - verilog_include_dirs:
      # Note: For .svh files the key `specific_files` is not functional yet.
      # For now, use `load_all_from` to include all files within a directory.
      - specific_files:
         - /path/to/file_1.svh
         - /path/to/file_2.svh
         - /path/to/file_n.svh

      - load_all_from:
         - /path/to/directory_1
         - /path/to/directory_2
         - /path/to/directory_n
   ```
   Note: For .svh files the key `specific_files` is not functional yet.
   For now, use `load_all_from` to include all files within a directory.


### 4. **simulator**
   - Specify the simulator to use for testing. Options: `'verilator'` or `'questa'`.
   - **Example**: `simulator: questa`

### 5. **timescale_timeprecision**
   - Defines the timescale and precision for the simulation. 
   - **Example**: `timescale_timeprecision: 1ns/1ps`

### 6. **DUT_name**
   - Names the Verilog module to be tested, without the `.sv` extension.
   - **Example**: `DUT_name: ALU_RV32I`

### 7. **template_name**
   - Specifies the name of the template the tool will use for the testbench.
   - **Example**: `template_name: tbs`

### 8. **DUT_inputs and DUT_outputs**
   - Define the **inputs** and **outputs** of the DUT:
      - **clocks** and **resets**: If your DUT requires clock or reset signals, define them in these lists.
      - List other input and output signals directly.
   - **Example**:
     ```yaml
     DUT_inputs:
       - clocks:
           - clk
       - resets:
           - rst
       - op
       - a  
       - b
     DUT_outputs:
       - o
     ```

### 9. **Error and Warning Messages**
   - Customize error and warning detection during the simulation using regular expressions.
   - **Example**:
     ```yaml
     error: (?i).*error.*
     warning: (?i).*warning.*
     ```

### 10. **quartus_project_path** (Optional)
   - If you are working with Quartus, provide the project path to facilitate synthesizability verification.
   - **Example**: `quartus_project_path: D:\path\to\quartus\project`

### 11. **synthesizability_command** (Optional)
   - Command used for synthesizability verification of the module.
   - **Example**: `synthesizability_command: quartus_sh --flow compile Logic_Circuit_Main`

### Instructions
1. Open PowerShell/Terminal in the `src` directory.
2. Run the following command:
   ```bash
   python .\cmd_controller.py path\to\yaml_file.yaml <flag>
   ```
   - If you run the command without any flags, the tool generates the template, the Makefile, and checks Quartus synthesizability.
   - Use the `-e` flag to execute the generated testbench template.
   - Use the `-r` flag to reset the template to its original state.
   - Use the `-i` flag to skip the Quartus synthesizability check.

3. **Output Generation**: The tool generates output files in the directory specified by the `output_dir` key in the YAML file.

### Notes
- **Verilator** assumes undefined input values as `0`.
- **Questa Intel FPGA Starter Edition** assumes undefined input values as `x`.