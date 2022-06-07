# Prim's algorithm (minimum spanning tree)
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Prim's algorithm (minimum spanning tree)](#prims-algorithm-minimum-spanning-tree)
    - [Pseudocode](#pseudocode)

<!-- markdown-toc end -->


## Pseudocode
```
function prim(G=V(V, E), s)

distance[1...n] = inf
parent[1...n] = null
T = T(V, null)
Q = PriotyQueue() // O(log(n)) time complexity for push and pop

distance[s] = 0
Q.add(0, key = s)

while PriotyQueue is not empty:
    // Works very similarly to dijkstra algorithm
    u = Q.pop() 
    // In dikjstra and other greedy algorithm, after popping from priority queue, it is finalised so add to result graph
    T.add_vertex(a)
    T.add_edge(E = (a, parent[a])) // parent of a is like a predecessor linking to a
    for each edge E = (u, v) adjacent to u:
        if distance[u] + w(u,v) < distance[v]:
            distance[v] = distance[u] + w(u,v)
            parent[v] = u
            // Update priority queue as well
            
return T
```
