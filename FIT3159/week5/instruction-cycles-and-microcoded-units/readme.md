# Instruction Cycles and Microcoded Control Unit, 
2022-03-28

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Instruction Cycles and Microcoded Control Unit,](#instruction-cycles-and-microcoded-control-unit)
    - [Why instruction cycles?](#why-instruction-cycles)
    - [Basic Machine organisation](#basic-machine-organisation)
        - [Central Processing Unit](#central-processing-unit)
        - [Main Memory](#main-memory)
        - [Input/Output (I/O)](#inputoutput-io)
    - [How is a program executed?](#how-is-a-program-executed)

<!-- markdown-toc end -->

## Why instruction cycles? 
* Control units are considered the heart of all modern computers
* Foundation knowledge all modern machines perform instruction fetch, decode and execute cycles in some fashion so understanding control units is essential
* Practical skills: programming in Assembly Language requires an understand of how a CPU (code) operates, especially **understanding control units is essential**.
* Practical skills: the performance of machines depends critically upon the design of the control unit.
* Practical skills: in real-time programming, many time critical portions of the code requires an understanding of the fetch/decode/execute cycle, an d how this impacts interrupt handling. 

## Basic Machine organisation
### Central Processing Unit
* Arithmetic logic unit
* Control Unit
* Register Files

### Main Memory
* TODO Memory Controller
* Memory Arrays

### Input/Output (I/O)
* I/O controllers
* I/O Devices

## How is a program executed?
* CPU **fetches** introductions (binary executable e.g. exe file) from the main memory
    * what is the different between data and code?

* Each instructions (e.g. add, load, store etc) must be **decoded** in the CPU

* Once the instruction is decoded in the CPU, it can be **executed ** by issuing commands in the ALU and manipulating operands in the CPU registers.

* Once the instruction is completed, another can be fetched from memory for execution.

* This cycle repeats for every instruction in the code
