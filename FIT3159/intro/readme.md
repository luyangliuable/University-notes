# Unit introduction and History of computer systems


<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Unit introduction and History of computer systems](#unit-introduction-and-history-of-computer-systems)
    - [Topics](#topics)
        - [Reading list](#reading-list)
    - [Linux Virtual Machine](#linux-virtual-machine)
    - [Electronic Computers](#electronic-computers)
    - [Moore's Law](#moores-law)
    - [Exponential Growth](#exponential-growth)

<!-- markdown-toc end -->


## Topics
* Machine arithmetic
* Micro-programming
* Caches
* Translation look aside buffers
* RISC machines
* and pipelines and parallel organisation (parallel system

## Objectives of unit

* Provide understanding in operating principle of a model digital computer
* Provide ability to understand the implications of **various designs upon hardware and computer system performance**.
* Provide ab ability to understand the **relationship between the architecture of the machine and its instruction set
* Provide the student with basic programming skills in **assembly machine language**
* **Tutorials are based on lectures**
* Each laboratories contribute 5%

### Reading list
* Stalling 8th Ed
* Mano and Kime 4th Ed
* Tanenbaum A S structured computer organisation 3rd Ed

## Linux Virtual Machine
* Unit info on Moodle
* Runs through Virtualbox 

## Electronic Computers

* Medium scale Integration (1970s) S-TTL, CMOs, NMOS, CPU
* Large Scale Integration (1980s) LS-TTL, CMOS, NMOS
* 1990s Microprocessors largely displace the minicomputer
* By Y2K, CMOs dominates, with millions of transistors per single Silicon die
* By 2010, CMOS technology multi core chips predominate with 2 or 4 reprocesses most cmmon.

## Moore's Law
> The number of transistors in the industry would be able to place on a computer chip would double every couple of years.
> -- Moore's Law

* initally intended as a rule of thumb in 1965, transformed into guiding principle for industry for ever-more-powerful semiconductor

## Exponential Growth

> Exponential growth occurs when the growth rate of the values of a mathematical function is proportional to the functions current value
> -- Wikipedia

```
x_t = x_0(1+r)^t
```

```
x(t) = x(b).e^(kt) = x(0).e^(t/tau)
```
* t, tau, rare constants constraining  the rate of growth over time
* often represented in logarithmic scale

## Example: IBM/Motorola G chip layout
* Data cache
* Integer Unit
* Cache Controller
* Instruction Sequencer
* Integer unit
* Load store unit
* Floating Point unit

## Exponential Growing mass storage technology
* Rotating "hard disks" continue to grow in the surface storage density following "**Kryder's Law**", exponentially.
* However, limited due to mechanical rotation and head movements (storage topics)
* SSD (Solid state disks) using flash RAM technology common to USB thumbdrive and SDHC models are becoming more affordable
* Flash RAM technology, SSDs will also follow the "Moores' law" exponential growth curve

* **Kryder's law** not only apply to capacity of storage but transfer speed of storage.
