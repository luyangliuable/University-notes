# Floyd Marshall algorithm
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Floyd Marshall algorithm](#floyd-marshall-algorithm)
    - [Pseudocode](#pseudocode)

<!-- markdown-toc end -->

## Pseudocode

```
function floyd_marshall(G=(V,E))

    dist[1...n][1...n] = inf
    dist[u][v] = w(u, v) for all edges e = (u,v) in E

    pred[1...n][1...n] = null
    pred[u][v] = v for all edges e = (u,v) in E

    for m in 1...n
        for u in 1...n
            for v in 1...n
                if dist[u][v] > dist[u][m] + dist[m][v] then
                    dist[u][v] = dist[u][m] + dist[m][v]
                    pred[u][v] = pred[u][m]
                    
    return dist[1...n][1...n], pred[1...n][1...n]
    
    
    
function backtrack_successor(u, v, pred)

    res = [u]
    while u != v
        u = pred[u][v]
        res.append(u)
        
    return res
```


## Time complexity
O(n^3) where n is the number of vertices

## Proof of correctness

## Invariant
* At all iterations of k, all the shortest paths in dist[1...n][1...n] contains the optimal/shortest paths not considering k+1 where 0 <= k+1 <= n.

* If there is no edge the path distance is inf.

## Starting
* At (k+1)th iteration, if there is a new path from u -> (k+1), (k+1) -> v. Then by inductive hypothesis, the new path would be an optimal path if it is shorter than u -> v which is inf.

* At (k+1)th iteration, if a shortcut is found via u -> (k+1), (k+1) -> v. Then by inductive hypothesis, the shortcut would be the optimal path.

## Termination
* Therefore after iteration k + 1, dist[u][v] contains the shortest path u -> v consisting of intermediate vertices from 1 to k + 1. 

* By induction on k, after iteration n, dist[u][v] contains the length of a shortest path u -> v consisting of any intermediate vertices, hence the distances are optimal.

