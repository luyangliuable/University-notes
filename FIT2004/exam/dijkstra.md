# Dijkstra algorithtm

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Dijkstra algorithm](#dijkstra-algorithm)
    - [Pseudocode](#pseudocode)
    - [Arguing Correctness](#arguing-correctness)
        - [Invariant](#invariant)
        - [Starting](#starting)

<!-- markdown-toc end -->



## Pseudocode

```
function dijkstra(G[|V|,|E|], s):

distance[1..n] = inf
pred[1..n] = 0

min_heap = min_heap

vertices_map = [0]*|V|

min_heap.add(s, key = 0)

while min_heap is not empty:
  u = min_heap.pop()
  for each edge = E(u, v) adjacent to u:
    if dist[v] < dist[u] + W(u, v):
        dist[v] = dist[u] + W(u, v)
        pred[v] = u
        
        min_heap.push(v, key=dist[v]) // The key is important to update the min_heap if the value of the distances are updated. Min_heap always return the smallest distance.
    
return distance[1...n], pred[1..n]
```

## Arguing Correctness

### Invariant
* All minimum vertices have their distances finalised

### Starting
* Min-heap only contains the source vertex at the start, this means the source vertex is finalised. We know that the distance from s -> s is always 0 so this is true.


* Therefore starting scenario is satisfied. TODO check if wording for **scenario** is correct.

## Maintenance
* After relaxing all the edges around a finalised vertex (e.g. source vertex). 

* Next smallest vertex is finalised because if the smallest direct path s -> b must be the shortest assuming that there is no negative path somewhere that would make other paths to b shorter. 

* This means s -> k -> b is shorter than s -> b which is impossible because s -> b is the shortest path currently in the min_heap and if s -> k -> b is short this means s -> k is the shorter path and k -> b must be relaxed before shortest path to b is determined.

* Therefore maintenance is satisfied


## Termination
* The termination condition for Dijkstra algorithm is that the min_heap is empty. This means that all the vertices are popped when their distances were all finalised. 

* If all the distances were finalised this means that the all the distances from source node correctly determined.
