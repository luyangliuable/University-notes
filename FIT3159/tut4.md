# Tut 4

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Tut 4](#tut-4)
    - [Operation of LDA instruction and time phase in cylce](#operation-of-lda-instruction-and-time-phase-in-cylce)
    - [Operation of JMS instruction](#operation-of-jms-instruction)
    - [Operation of Load/Store instruction](#operation-of-loadstore-instruction)
        - [Load instruction](#load-instruction)
        - [Question 3](#question-3)
    - [Kryders law vs Moore's law](#kryders-law-vs-moores-law)
    - [Explain the differences between raid 0 and raid 1](#explain-the-differences-between-raid-0-and-raid-1)

<!-- markdown-toc end -->


## Operation of LDA instruction and time phase in cylce
T4
– Instruction Register ->CPU Bus;
– CPU Bus -> Memory Address
Register
• T5
– Memory Address Register ->
Address Bus:
– Control Signal ->Control Bus
• T6
– Memory Data -> Memory Read
Register (via Data Bus)
• T7
– Memory Read Register ->
Accumulator Register


## Operation of JMS instruction
JMS is a jump instruction where you are using the accumulator to change the project counter to jump to specific locations inside the program

T1: 
* Program counter to CPU bus
* CPU bus to accumulator

T2:
* Instruction register -> CPU bus
* CPU bus -> Program counter

The previous program counter value must be saved before the new one is loaded.

## Operation of Load/Store instruction
### Load instruction
T1: 
* Instruction


### Question 3

a. Polling is the easiest method we can use. You only have to use a loop. Servicing requires additional hardware.

b. You cannot interrupt a CPU during a multiple CPU cycle.

c. Microword to add little bits to check the instructions as well.

Vector interrupts. For hard disk devices you can same memories but you need extra jumps inside CPU cycles.


DMA: DMA is interrupt driven I/O. It is used to take away the CPU overhead. We need to interrupt the CPU at the end of the CPU. Once the DMA controller _ is configured, the CPU must be interrupt to notify the _ it is ready to be used.


DMA is primary used to deal with the hardware. DMA uses polling system.

## Kryders law vs Moore's law
Shorter access time

## Explain the differences between raid 0 and raid 1

In raid controller, reliability and speed are important.

In raid 0 controller, because it uses striping, if you connect a 1TB hard drive with a 800GB hard drive. Only 800GB of the 1 TB will be used in the 1TB. The other 200GB will be redundant.

| Raid 0          | Raid 1 |
|:---------------:|:------:|
| Speed is faster |        |
|                 |        |
|                 |        |
|                 |        |
|                 |        |
|                 |        |


## 5
### a

4 Disks
* 2TB $119

Raid 5,
* Effective storage capacity: 6TB (5.45 TiB)
* Cost per TB: $66.67
    * 400/6 = $66.67
* Disk efficiency: 75%
* Usable capacity of single RAID group: 6TB
* Fault tolerance per RAID group: 1
* Total number of drives: 4
* Read speed gain: 4x
* Write speed gain: 1x

Raid 6
* Effective storage capacity: 4TB (3.64 TiB)
* Cost per TB: $100
    * 400/4 = $100
* Disk efficiency: 50%
* Usable space efficiency: 50%
* Usable capacity of single RAID group: 4TB
* Fault tolerance per RAID group: 2
* Total number of drives: 4
* Read speed gain: 4x
* Write speed gain: 1x

| Raid 6                                | Raid 5 |
|:-------------------------------------:|:------:|
| Raid 6 has large and reliable storage |        |
|                                       |        |


Example:
2TB HDD
7200 rpm
Average seek time: 2ms

*Find average process time:*
7200/60 =  120 round per second

1/120 = 0.0083 = second per round

1/240 = second per half a round
0.00416 = second per half a round

0.00416 + 2ms = 0.00616 seconds
