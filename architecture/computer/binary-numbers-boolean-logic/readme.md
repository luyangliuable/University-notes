# Binary Numbers Boolean Logic
    
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Binary Numbers Boolean Logic](#binary-numbers-boolean-logic)
    - [Why boolean logic?](#why-boolean-logic)
    - [Binary logic and gates](#binary-logic-and-gates)
    - [Binary variables](#binary-variables)
    - [Operator Definitions](#operator-definitions)
    - [Truth Tables](#truth-tables)
    - [Logic function implementation](#logic-function-implementation)
    - [Logic gates](#logic-gates)
        - [Earliest days (computers)](#earliest-days-computers)
        - [Later (computers)](#later-computers)
        - [Today (computers)](#today-computers)
    - [Gate Delay](#gate-delay)
    - [Boolean equations, truth tables, logic diagrams](#boolean-equations-truth-tables-logic-diagrams)
    - [Algebraic laws](#algebraic-laws)
    - [Minterm and Maxterm](#minterm-and-maxterm)

<!-- markdown-toc end -->

## Why boolean logic?
* Computers consists of digital logic circuits and components
* Understanding how data is represented

## Binary logic and gates
* Binary logic consists of two states (either 1 on or 0 off**
* Basic logical operators are the logic functions AND, OR and NOT 
* Logic operators operate on binary values and binary variables
* Boolean algebra in this FIT3159 is used to analyse digital systems.

## Binary variables
* True/False
* On/Off
* Yes/No
* 1/0

| word representation | symbol simple | symbols |
|---------------------|---------------|---------|
| AND                 | .             | ˜       |
| NOT                 | '             | TODO    |
| OR                  | +             | TODO    |

## Operator Definitions
* Operators are defined on the values 0 and 1 for each operator

| OR      | NOT    | AND     |
|---------|--------|:-------:|
| 0+0 = 0 | 0' = 1 | 0.0 = 0 |
| 0+1 = 0 | 1' = 0 | 0.1 = 0 |
| 1+0 = 1 |        | 1.0 = 0 |
| 1+1 = 1 |        | 1.1 = 1 |

## Truth Tables

| AND |   |       |
|:---:|:-:|:-----:|
| X   | Y | X=X.Y |
| 0   | 0 | 0     |
| 0   | 1 | 0     |
| 1   | 0 | 0     |
| 1   | 1 | 1     |


| OR |   |       |
|:--:|:-:|:-----:|
| X  | Y | X=X+Y |
| 0  | 0 | 0     |
| 0  | 1 | 1     |
| 1  | 0 | 1     |
| 1  | 1 | 1     |


## Logic function implementation
* Using switches 
  * For inputs:
    * logic 1 is **switch closed**
    * logic 0 is **switch open**
  * For outputs
    * For inputs:
      * logic 1 is light on
      * logic 0 is light off
  * NOT uses a **switch such that**
    * logic 1 is **switch open**
    * logic 0 is **switch closed**

## Logic gates

* There exists many transistor types, current preference is CMOS due to **low power drain**.

### Earliest days (computers)
Switches were opened and closed by magnetic fields produced by energising coils in relays.

### Later (computers)
Vacuum tubes open and close current paths electronically replaced relays

### Today (computers)
Transistors are used as electronic switches that open and close current paths

## Gate Delay
In actual physical gates, if one or more input changes causes the output to change does not occur instantaneously.
The **delay between an input change and the resulting output change** is the gate delay t_G.
TODO why is this important

## Boolean equations, truth tables, logic diagrams
* Boolean equations, truth tables and and logic diagrams describe the same function!

## Algebraic laws

|           |         |              |
|:---------:|:-------:|--------------|
| X+0       | X       |              |
| X+1       | 1       |              |
| X+X       | X       |              |
| X+X'      | 1       |              |
| X''       | X       |              |
| X.1       | X       |              |
| X.0       | 0       |              |
| X.X       | X       |              |
| X.X'      | 0       |              |
| X+Y       | Y+X     | Commutative  |
| XY        | TX      | Commutative  |
| (X+Y)+Z   | X+(Y+Z) | Associative  |
| X(Y+Z)    | XY+XZ   | Distributive |
| '( X+Y )  | 'X+''Y  | DeMorgans    |
| ''( X.Y ) | 'X+'Y   | DeMorgans    |

## Minterm and Maxterm

* Minterm: The logical AND or logical product of two or more Boolean variables or the complements of these variables
  * e.g. A.B.C, A'.B.C and AB'C
  
* Maxterm: The logical OR or logical sum of two or more Boolean variables or the complements of these variables
  * A+B+C, A'+B+C, A+B'+C 

## Boolean expression order of evaluation

1. PARENTHESIS
2. NOT
3. AND
4. OR
