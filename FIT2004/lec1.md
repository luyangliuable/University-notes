# Introduction
2022-02-28T14:06:29+11:00


<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Introduction](#introduction)
    - [Purpose of FIT2004](#purpose-of-fit2004)
    - [Expectations](#expectations)
    - [Most important algorithm design paradigms](#most-important-algorithm-design-paradigms)
    - [Books](#books)
    - [Divide and conquer](#divide-and-conquer)
    - [Multiplication algorithm](#multiplication-algorithm)
        - [First Improvement Idea](#first-improvement-idea)
    - [Complexity Analysis](#complexity-analysis)

<!-- markdown-toc end -->

## Purpose of FIT2004
* Solving problems with computers efficiently
* Developing algorithms toolbox
* Training your problem solving skills
* Deepening understanding of how the working of a computers relate to algorithm speed
* **Not mainly** about programming
* Mainly use python as the programming language but in general **language agnostic**
* Algorithms will be presented in English, pseudo code, procedural set of instructions or python

## Expectations
* Very **important for computer and technology related careers**
* Big tech companies hunt for people who are proficient at  algorithms and data structures
* Many interview question are based on algorithms from this unit
* Many studio questions are very similar to questions asked in job interviews (e.g. Google, leetcode interviews)
* This unit is **challenging**

## Most important algorithm design paradigms
* Divide and conquer
* Greedy algorithms
* Dynamic programming
* Network flow
* Analysis of algorithms
* Learn important data structures for implementing algorithms efficiently
* Selection of important algorithms
  * Sorting
  * Retrieval
  * Shortest path on maps

TODO FIT2004 Course Notes, ED forums

## Books
* CLRS: Thomas H. Cormen, *Introduction to Algorithms*
* Rou: Time Roughgarden *Algorithms illuminated*
* KT: Jon Kleninberg *Algorithm design*
* Knu: Donalds Knuth *The art of computer programming*

## Divide and conquer

1. Divide problem into smaller sub-problems
2. solver the smaller sub-problems
3. Combine the solutions of the smaller problems to the solutions of the bigger problem

* Involves solving a **recurrence relation**

* Normally polynomial is used to reduce the time complexity to a lower polynomial

## Multiplication algorithm

### First Improvement Idea

* Split the numbers between the n/2 most significant digits and the n/2 least significant digits; and do recursive calls with them.


### Karatsuba's Algorithm


## Complexity Analysis

The amount of time taken by an algorithm to run as a function of the input size

* Worst-case complexity (main focus)
* Best case complexity
* Average case complexity

### Big-O Notation

* f(n) = O(g(n)) if there are constant c and n_0 such that:
  * f(n) <= c.g(n) for all n >= n_0

* Big-Omega f(n) = Omega(g(n)) if there are constant c ad n_0

TODO

### Space complexity analysis

#### Space complexity
The amount of space taken by an algorithm as a function of input size

#### Auxiliary space complexity
The amount of space taken by algorithm excluding the space taken by input

### In place algorithm
An algorithm that has O(1) auxiliary space complexity (e.g. Merge sort is not an in place algorithm as it needs to create output list)

``` python
min = [1]
index = 2

while index <=N:
    if index < min:
        min = array[index]
    index 
```

TODO Fast Fourier Transform (not covered in unit)

TODO recursive fibonnaci

TODO Section 1.2, 1.3, 1.4, chapt. 2
