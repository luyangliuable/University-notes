# Week 6 studio sheet
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Week 6 studio sheet](#week-6-studio-sheet)
    - [Problem 1 Shortest path using dijkstra's algorithm](#problem-1-shortest-path-using-dijkstras-algorithm)
- [Problem 2](#problem-2)
    - [Prims algorithm](#prims-algorithm)
    - [kruskals algorithm](#kruskals-algorithm)
- [Problem 3](#problem-3)
    - [union(3, 6)](#union3-6)
    - [union(0, 5)](#union0-5)
    - [union(5, 3)](#union5-3)

<!-- markdown-toc end -->

## Problem 1 Shortest path using dijkstra's algorithm

dict = {"p": 0, "q": 1, "r": 2, "s": 3, "t": 4, "u": 5, "v": 6, "w": 7, "x": 8, "y": 9, "z": 10}

s: distance = 0
w: distance = 18
y: distance = 3

pop y:
w: distance = 17 update
v: distance = 18
x: distance = 18

pop w:
t: distance = 17 + 14 = 31

pop v:
z: distance = 10 + 18 = 28
t: distance = 18 + 6 = 24 update
u: distance = 5 + 18 = 23

pop x:
v: distance = still 18
u: distance = still 23

pop t: 
q: distance = 31 + 12 = 43

pop u:
z: distance = 23 + 4 = 27 update
r: distance 23 + 11 = 34

pop z:
q: distance = 27 + 1 = 28 update
p: distance = 27 + 7 = 34
r: distance = 27 + 2 = 29 update

pop q:
p: distance = 33 update from 34

pop r:
p: distance = still  33

pop p:
p: distance = still 33

over!

dist = [33, 34, 33, 0, 24, 23, 18, 18, 18, 3, 27]


# Problem 2

## Prims algorithm

vertex a:
d: distance = 2
parent = a

b: distance = 5
parent = a

pop d:
e: distance = 16
parent = d
f: distance = 4
parent = d

pop f:
e: distance = 8
parent = f
g: distance = 10 update
parent = f

pop b:
e: distance = 1 update
parent: b
c: distance = 8
parent: b

pop e:
g: distance = 9 update
parent: e

pop c:

parent = [a, a, b, a, b, d, e]
dist = [0, 5, 8, 2, 1, 4, 9]

## kruskals algorithm
union(b, e)
id = [0, 1, 2, 3, 4, 5, 6]
parent = [0, 1, 2, 3, 1, 5, 6]

union(a, d)
id = [0, 1, 2, 3, 4, 5, 6]
parent = [0, 1, 2, 0, 1, 5, 6]

union(d, f)
id = [0, 1, 2, 3, 4, 5, 6]
parent = [0, 1, 2, 0, 1, 3, 6]

union(e, c)
id = [0, 1, 2, 3, 4, 5, 6]
parent = [0, 1, 2, 0, 1, 3, 6]

union(a, b)
id = [0, 1, 2, 3, 4, 5, 6]
parent = [0, 0, 4, 0, 1, 3, 6]

union(e, f)
id = [0, 1, 2, 3, 4, 5, 6]
parent = [0, 0, 4, 0, 1, 3, 6]

union(e, g)
id = [0, 1, 2, 3, 4, 5, 6]
parent = [0, 0, 4, 0, 1, 3, 4]

parent = [a, a, b, a, b, d, e]



# Problem 3


## union(3, 6)
id = [0, 1, 2, 3, 4, 5, 6, 7, 8]
parent = [-1, 2, -3, -1, 7, -1, 7, -4, 2]


## union(0, 5)
id = [0, 1, 2, 3, 4, 5, 6, 7, 8]
parent = [5, 2, -3, -1, 7, -2, 7, -4, 2]

## union(5, 3)
id = [0, 1, 2, 3, 4, 5, 6, 7, 8]
parent = [-1, 2, -3, 5, 7, -4, 7, -4, 2]
/Users/rubber/University-notes/FIT2004/shortest_path/
