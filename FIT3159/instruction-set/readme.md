# Instruction set
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Instruction sets](#instruction-sets)

<!-- markdown-toc end -->


## Why study this?

* Insutrction set design impacts performance and functionality of all modern computers

* Foundatational knowledge: understand the difference between instruction sets and impact on performance and CPU deisgn

* Foundation knowledge: reinforce unstanding of control units and relationships between instruction sets and control unit designs

* Practical skills: Assembly code programming - understand what instructions actually do and how they work

* Practical skills: Assembly code programming - understanding how instrucitons work allows you to write assembler for any arbitrary machine architecture.


## Busses and registers

* A register in a cpu typically uses two control signals
    * One signal latches a value from the cpu bus into the register
    * the other assert the contents of the register on the CPU bus
    
* Therefore only two bits in the microword are required to control the register

* Typically only one source device and on destination device can be used on such a bus.
