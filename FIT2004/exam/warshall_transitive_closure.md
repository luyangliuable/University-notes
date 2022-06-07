# Warshall Transitive Closure
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Warshall Transitive Closure](#warshall-transitive-closure)
    - [Pseudocode](#pseudocode)
    - [Time Complexity](#time-complexity)

<!-- markdown-toc end -->

## Pseudocode
```
function transitive_closure(G=(V,E))
    connected[1...n][1...n] = 0
    
    for each v in 1...n do
        connected[v][v] = 1 # Store using bitvector
        
    
    for every edge e = (u,v) in E do
        connect[u][v] = 1
        
        
    for k in 1...n do
        for u in 1...n do
            for v in 1...n do
                connected[u][v] = connected[u][v] or (connected[u][k] and connected[k][v])
                

    return connected[1...n][1...n]
```

## Time Complexity
O(|V|^3/w) where |V| is the number of vertices in the graph and w is the number of bits in machine word.


## Invariant
* At all times, the connected[1...n][1...n] matrix stores all the connected vertices considering 1...k intermediary vertices where 1 <= k <= n.

## Starting
* The connected[1...n][1...n] only contains single edges that links two vertices. Using no intermediary vertices at all this is the optimal solution.

## Maintenance
* If a new path using intermediary path k+1, u->k+1, k+1 -> v. Then this would indicate u and v are connected. 

* By inductive hypothesis, connnected[u][v] is not connected if there is no intermediary path that links u and v.
* If there  is a intermediary path, then connnected[u][v] is connected
* Hence we have an optimal solution.

## Termination
* By induction on k, after iteration n, connnected[u][v] contains the connected path linking u -> v consisting of any intermediate vertices, hence the results are optimal.
