# Question 1

Moores law is important because it states that the computational speed of cpu will increase exponentially due to the doubling of number of transistors. This is an exponential law but turning into a linearly law. Transistors are proportional to power, meaning more transistors and more calculations per unit of time

| X.Y.X | X+Y+Z | X' | Y' | Z' |
|:-----:|:-----:|:--:|:--:|:--:|
| 0     | 0     | 1  | 1  | 1  |
| 0     | 1     | 1  | 1  | 1  |
| 0     | 1     | 1  | 0  | 0  |
| 0     | 1     | 0  | 1  | 1  |
| 0     | 1     | 0  | 1  | 0  |
| 0     | 1     | 0  | 1  | 0  |
| 0     | 1     | 0  | 0  | 1  |
| 1     | 1     | 0  | 0  | 0  |


| X+Y'.Z | X.Y.Z' | X+Y'Z | Y' | Z' |
|:------:|:------:|:-----:|:--:|:--:|
| 0      | 0      | 0     | 1  | 1  |
| 1      | 0      | 1     | 1  | 0  |
| 0      | 0      | 0     | 0  | 1  |
| 0      | 0      | 0     | 0  | 0  |
| 1      | 0      | 1     | 1  | 1  |
| 1      | 0      | 1     | 0  | 1  |
| 1      | 1      | 1     | 1  | 0  |
| 1      | 0      | 1     | 0  | 0  |

# Order of evaluation for Boolean expressions

First comes parenthesis. For Boolean expressions, not expressions come first, you will need to first inverse the signal. Next comes the and expressions followed by or. Finally, you need to worry about 

# Written and in class: What is Gate Delay and why is it important? Explain in less than 100 words.
The longest length of time for the input signal to reach to the each of the gate. Time different between input and output to occur. It is important because this means that the getting the result of a logic gate is not instantaneous (i.e. takes time).

