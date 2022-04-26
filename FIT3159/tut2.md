# Tutorial Week 3
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Tutorial Week 3](#tutorial-week-3)
    - [Question 1](#question-1)
        - [For typical 8 bit machine](#for-typical-8-bit-machine)
        - [For typical 16 bit machine](#for-typical-16-bit-machine)
        - [For typical 32 bit machine](#for-typical-32-bit-machine)
        - [For typical 64 bit machine](#for-typical-64-bit-machine)
        - [Added two numbers in a base 2 floating point representation](#added-two-numbers-in-a-base-2-floating-point-representation)
            - [Example 0.375 + 0.125](#example-0375--0125)
        - [Multiplying two numbers in a base 2 floating point representation](#multiplying-two-numbers-in-a-base-2-floating-point-representation)
    - [2c. Little vs big endian](#2c-little-vs-big-endian)
    - [Question 2 difference between an 8bit, 16bit, 32bit, and 64bit datapath machine](#question-2-difference-between-an-8bit-16bit-32bit-and-64bit-datapath-machine)
    - [Question 3a](#question-3a)
    - [Question 3b](#question-3b)
    - [Question 4a shifter example](#question-4a-shifter-example)
    - [Question 4b adder example](#question-4b-adder-example)
    - [Question 5a SR-latch example](#question-5a-sr-latch-example)
    - [Question 5b D-latch](#question-5b-d-latch)

<!-- markdown-toc end -->

## Question 1

### For typical 8 bit machine
Char: 8
Short: 4
Int: 8
Long: 32
Float: 32

### For typical 16 bit machine
Char: 8
Short: 8
Int: 16
Long: 32
Float: 32

### For typical 32 bit machine
Char: 8
Short: 16
Int: 32
Long: 32
Float: 32

### For typical 64 bit machine
Char: 8
Short: 16
Int: 32
Long: 32
Float: 32

### Added two numbers in a base 2 floating point representation
Added two numbers involves denormalising the mantissas (making exponents the same), then adding. After which you have to normalise the mantissas again

#### Example 0.375 + 0.125

0.375 mantissa is 110000....., exponent is 11111111
0.175 mantissa is 010000....., exponent is 11111110

Add:
mantissa is 100000....., exponent is 00000000
1*0.5 = 0.5

### Multiplying two numbers in a base 2 floating point representation
This involves multiplying only the mantissas and them simply adding the exponent. You also need to normalise. 

Adding is more complicated than multiplying because there are extra steps involved for adding.

TODO use calculator to learn multiply and add two hexadecimal number

## 2c. Little vs big endian
Endian is the order where bytes are arranged in the memory. Alternatively it can be referred to as byte ordering

Big Endian **has the most significant byte as the lowest address**.

Little Endian **has the lowest significant byte as the lowest address**.

There is no different in advantage between the two as they are simply different architectures.


## Question 2 difference between an 8bit, 16bit, 32bit, and 64bit datapath machine
Datapath is responsible for taking data in and out of memory determined by the control lines while the bus control lines point to the current data.

If a data path is 8bits, this means all 8 bits (a byte) will be read simultaneous during read operation. This is a byte address bar memory

During write operation. the address must be correctly set to corresponding address bus control lines. This means that have more bits will increase the size of memory and increase the size of the datapath will increase the amount of data that can be read simultaneous hence increasing the read/write speeds.

## Question 3a

Z = f(A,B) = A'B' + AB' + A'B

| B\A | 0 | 1 |
|:---:|:-:|:-:|
| 0   | 1 | 1 |
| 1   | 1 | 0 |

f(A, B) = B' + A'B = y' + x'

## Question 

| Static logic hazard                                                                                                                                                           | dynamic logic hazard                                                                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Occurs when diiferent paths in a circuit has different delays from input to output, this leads to disturbances where the output does not instantly show up due to logic gates | This occurs when a number of static hazard exist inside a complex logic circuit. This can cause many disturbance or fluctuation to show up in the logic gate |
|                                                                                                                                                                               |                                                                                                                                                              |

Hazards arise because of logic gate delay leading to output prematurely getting the wrong output until all the delay are settled and the correct output according to the logic gate is finally shown. This can be resolved by using karnaugh maps to identify hazards and introducing more logic gates that does not affect the function while still eliminating the hazard.

## Question 4a shifter example

11010101
D0: 1
D1: 0
D2: 1
D3: 0
D4: 1
D5: 0
D6: 1
D7: 1

Shift left:
S0: 0 is right.D1
S1: 1 is left.D0
S2: 0 is left.D1
S3: 1 is left.D2
S4: 0 is left.D3
S5: 1
S6: 0
S7: 1

10101010

## Question 4b adder example

A = 1101
B = 1001

A0 = 1
B0 = 1

A1 = 0
B1 = 0

A2 = 1
B2 = 0

A3 = 1
B3 = 1

S0 = 0
Cout = 1

S1 = 1
Cout = 0 

S2 = 1
Cout = 0

S3 = 0
Cout = 1

S4 = 1

output = 10110

## Question 5a SR-latch example

S = 1
Q' = 0
so R' + Q' = 1 = Q

S = 0

Q' = Q' + S = 0


R = 1
Q = R' + Q' = 0
Q' = S + Q = 0 + 1 = 1
R = 0
Q = Q' + R = 0 + 0 = 0

## Question 5b D-latch

Clock = 1
Q' = 0
Q = 0
D = 1

Q' = 0
Q = 1

Clock = 0
Q' = 1
Q = 0

Clock = 1
Q' = 0
Q = 1

