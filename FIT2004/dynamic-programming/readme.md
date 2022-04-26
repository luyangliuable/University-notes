# Assessed preparation Week 7 studio sheet

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Assessed preparation Week 7 studio sheet](#assessed-preparation-week-7-studio-sheet)
    - [Problem 2](#problem-2)
        - [Optimal Substructure](#optimal-substructure)
        - [Overlapping Subproblems](#overlapping-subproblems)
        - [Base case subproblems](#base-case-subproblems)
        - [Recurrence relation describing the solutions to the subproblems](#recurrence-relation-describing-the-solutions-to-the-subproblems)
            - [Recurrent relation for solution to current neighbour:](#recurrent-relation-for-solution-to-current-neighbour)
            - [Recurrence relation for time complexity:](#recurrence-relation-for-time-complexity)
        - [Pseudocode:](#pseudocode)

<!-- markdown-toc end -->


## Problem 2

### Optimal Substructure
The maximum of previous earning of door to door sales without having consecutive neighbours.



### Overlapping Subproblems
You have subproblems where you have to find all the previous max earning of door to door sales leading up to the current position in the neighbourhood.


### Base case subproblems
Base case is 0 because at the start (before knocking on any doors) you don't have any earnings 


### Recurrence relation describing the solutions to the subproblems
#### Recurrent relation for solution to current neighbour:
total_profit[j] = max(total_profit[j], total_profit[j-i] + price[j])
* Where i is the previous door

#### Recurrence relation for time complexity:
T(n) = T(n-1) + a if n > 0
T(n) = b if n = 0

### Pseudocode:


```
function door_to_door(num_of_houses, price [1...N]):
    total_profit[1...num_of_houses] = 0

    for i = 1 to N do
        for j = i + 2 to N do
            total_profit[j] = max(total_profit[j], total_profit[j-i] + price[j])
            i = j # Jump to the next neighbour that get sold

    return total_profit
```
