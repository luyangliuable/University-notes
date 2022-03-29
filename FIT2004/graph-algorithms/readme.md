# Graph algorithms
## Prim's algorithms

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Graph algorithms](#graph-algorithms)
    - [Prim's algorithms](#prims-algorithms)
    - [Inductive Step](#inductive-step)
    - [Kruskal's algorithm](#kruskals-algorithm)

<!-- markdown-toc end -->

## Inductive Step

* We want to show that if T is a subset of some MST at the start of some iteration, it is still a subset of some MST at the start of the next iteration.o

* Since M is a tree, there is exactly one path from u to v in M (shown in blue)

* u and v are not connect in T (since v is not in T). Consider the first edge on the blue path which is not contained in T (call this edge x)

* One vertex of this edge is in T, the other is not.

* Removing this edge would disconnect M

* Add in edge (u,v) would form a new spanning tree M

* Since the algorithm always selects the lights edge incident to T we know that w(e) <= w(x)

* So the weight of M is no greather than the weight of M, therefore choosing e is correct


## Kruskal's algorithm

* Spannign tree finding algorithms

``` Pseudocode
Kurskals(G(V,E)):
    Sort the edges in ascending order of weights
    Let T be a graph with V as its vertics and no edges
    For each edge (v, u) in aascending order 
        if adding (v, u) does not create a cycle in T
            Add (v,u) to T
            
    return T
```
