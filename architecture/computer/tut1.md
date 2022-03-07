# Tutorial 1
Due date: 2022-03-04 

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Tutorial 1](#tutorial-1)
    - [Question 1](#question-1)
        - [Written and in class: Explain in 100 words Moore's Law, and why it is important](#written-and-in-class-explain-in-100-words-moores-law-and-why-it-is-important)
            - [Moore's law](#moores-law)
            - [Why is Moore's law important?](#why-is-moores-law-important)
    - [Question2](#question2)
        - [Order of evaluation for Boolean expressions](#order-of-evaluation-for-boolean-expressions)
    - [Question3](#question3)
        - [Written and in class: What is Gate Delay and why is it important? Explain in less than 100 words.](#written-and-in-class-what-is-gate-delay-and-why-is-it-important-explain-in-less-than-100-words)
            - [What is gate delay?](#what-is-gate-delay)
            - [Why is it important?](#why-is-it-important)

<!-- markdown-toc end -->

## Question 1 
### Written and in class: Explain in 100 words Moore's Law, and why it is important

#### Moore's law
Moore's law states that the computational speed of cpu will increase exponentially due to the doubling of number of transistors and advancement in power conservation and battery technologies. 

This is an exponential law but often shown in logarithmic scale so it appears linear on the graph. 

Transistors are proportional to power, meaning more transistors means more power consumed but more calculations per unit of time. However this is still an effect observed in semiconductor monolithic technologies so it should be regarded as an effect rather than law.


#### Why is Moore's law important?
This is important because it means that the advancement in computational speed of modern components is increasing exponentially. We could have a computer that's many magnitudes faster that this year's computer many years later. This could imply that computer will become obsolete faster and technologies companies can make more money off consumers through moore's law alongside planned obsoletion. The good news is that, fast computational speed means access to better solutions to world problems such as discovering new drugs and cures, AI classifiers, and software.

Correct

| X | Y | Z | X.Y.X | X+Y+Z | X' | Y' | Z' |
|---|---|---|:-----:|:-----:|:--:|:--:|:--:|
| 0 | 0 | 0 | 0     | 0     | 1  | 1  | 1  |
| 0 | 0 | 1 | 0     | 1     | 1  | 1  | 0  |
| 0 | 1 | 0 | 0     | 1     | 1  | 0  | 1  |
| 0 | 1 | 1 | 0     | 1     | 1  | 0  | 0  |
| 1 | 0 | 0 | 0     | 1     | 0  | 1  | 1  |
| 1 | 0 | 1 | 0     | 1     | 0  | 1  | 0  |
| 1 | 1 | 0 | 0     | 1     | 0  | 0  | 1  |
| 1 | 1 | 1 | 1     | 1     | 0  | 0  | 0  |

Correct

| X | Y | Z | X+Y'.Z | X.Y.Z' | X+Y'Z | Y' | Z' |
|---|---|---|:------:|:------:|:-----:|:--:|:--:|
| 0 | 0 | 0 | 0      | 0      | 0     | 1  | 1  |
| 0 | 0 | 1 | 1      | 0      | 1     | 1  | 0  |
| 0 | 1 | 0 | 0      | 0      | 0     | 0  | 1  |
| 0 | 1 | 1 | 0      | 0      | 0     | 0  | 0  |
| 1 | 0 | 0 | 1      | 0      | 1     | 1  | 1  |
| 1 | 0 | 1 | 1      | 0      | 1     | 1  | 0  |
| 1 | 1 | 0 | 1      | 1      | 1     | 0  | 1  |
| 1 | 1 | 1 | 1      | 0      | 1     | 0  | 0  |

## Question2
### Order of evaluation for Boolean expressions

The order for evaluation of Boolean expressions.
1. Parenthesis or brackets
2. NOT
3. AND
4. OR

This means that parenthesis often appear in front of OR because it is of the least priority for evaluation. Also we often can see parenthesis in front of AND followed by NOT.

Example: R = A.(B.C)'(C + D)

## Question3 
### Written and in class: What is Gate Delay and why is it important? Explain in less than 100 words.
#### What is gate delay?
The longest length of time for the input signal to reach to the each of the gate. Time different between input and output to occur. 


#### Why is it important?
It is important because this means that the getting the result of a logic gate is not instantaneous (i.e. takes time). So if you have a lot of logic gates in the circuit it could hinder the time to get the result and increase the gate delay. The number of logic gates in the circuit matters so save time and cost meaning it is often better to come up with the most simple circuit and correct circuit.
