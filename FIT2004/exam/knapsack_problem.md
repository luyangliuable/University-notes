# Knapsack problem

subproblem = {The weight of smaller components}

optimal substructure:

0, if capacity is smaller than W_i for all i
Max(DP[w], DP[c - W[i]] + v[i])

## Unbounded Knapsack
### Pseudocode
```
function knapsack(v[1...n], W[1...n], C)
    DP[1...n] = 0
    
    
    for c in 1...C:
        for i in 1...n:
            if c >= w[i]: // If capacity is enough for the given weight
                DP[i] = max(DP[i], v[i] + DP[C - w[i]])
                
    return DP[C] // Return value at max capacity
```
    
## 0-1 Knapsack
Can only use each item once.

Optimal substructure
0, if i == 0
max_value[i-1][c], if w_i > C
max(max_value[i-1][c], v[i] + max_value[i-1][c-w[i]]), otherwise

### Pseudocode
```
function knapsack(v[0...n], W[0...n], C)
    DP[0...n][0...C] = 0
    
    for i in 0...n:
      for c in 0...C:
        if i == 0 or c == 0:
            DP[i][c] = 0

            if c >= w[i-1]: // If capacity is enough for the given weight
                DP[i][c] = DP[i-1][c]
            else:
                DP[i][c] = max(DP[i-1], v[i-1] + DP[C - w[i-1]])
                
    return DP[n][C] // Return value at max capacity
```
