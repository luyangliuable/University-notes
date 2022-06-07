# Kruskal algorithm
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Kruskal algorithm](#kruskal-algorithm)
    - [Kruskal's minimum spanning tree algorithm](#kruskals-minimum-spanning-tree-algorithm)
    - [Union Finding](#union-finding)
        - [Find](#find)
            - [Pseudocode](#pseudocode)
    - [Union By rank](#union-by-rank)
    - [Union by compression](#union-by-compression)

<!-- markdown-toc end -->

## Kruskal's minimum spanning tree algorithm

```
function kruskal(G=(V,E))
    sort(E, key((u,v)) = w(u,v))
    // Always prioritise the smallest edges which checking for unions.

    forest = UnionFind.initalise(n)
    
    result_tree = (V, null)
    
    for each E = (u, v) in sorted G do
        // Basically the key idea is to skip unions because this means there is already on the result tree that joins to v.
        if find(u) != find(v) then
            forest.union(u, v)
            result_tree.add_edge(u, v)
            
    return result_tree

```

## Proof of correctness

### Useful invariant
* Kruskal always use sorted edges by weight or priority queue to always use the smallest edge.

* Kruskal won't consider any vertices that form a cycle with finalised edges. This is done by checking using find and see if the parent are the same.

* At all times, kruskal maintains a spanning tree with the smallest weight by consideration the smallest edges first and avoiding forming a cycle anywhere.

### Starting
* At the start the result tree is empty, this is empty but still a minimum spanning tree so it is maintained.
* Empty graph does not contain a cycle.

### Maintenance
* If the parent of the new vertex v != parent of vertex u, either a bridge is going to be formed or a new vertex is being considered. 

* Either case, no new cycle would form as a result. If parent is the same, linking the two together would result in a cycle.

* Only the smallest weighted edge is considered to replicated a bottleneck path to help create the minimum spanning tree.

### Termination
* All the sorted edges are checked. Also the all larger edges that would result in a cycle (not linking to new vertices or forming bridges) are ignored. Hence the algorithm terminates with a correct minimum spanning tree.

## Union Finding

### Find

#### Pseudocode
```
function init(n):
    parent[1...n] = 1...n
    
    
function find(n):
    // Find the parent of n
    
    if parent[n] != n
        return find(parent[n])
        
    return n
    
    
function union(x, y):
    parent_of_x = find(x)
    parent_of_y = find(y)
    parent[parent_of_x] = parent_of_y

```

## Union By rank
* Each val in parent array stores the number of items under the parent.

```
function init(n)
    parent[1..n] = 1...n
    rank[1..n] = 0

function find(n)
    // Same deal and normal union
    // Find the parent of n
    
    if parent[n] != n
        return find(parent[n])
        
    return n
    
    
function union(x, y)
    parent_of_y = find(y)
    parent_of_x = find(x)
    
    rank_of_y = rank[parent_of_y]
    rank_of_x = rank[parent_of_x]
    
    if rank_of_y > rank_of_x then
        parent[parent_of_x] = parent_of_y
    else:
        parent[parent_of_y] = parent_of_x
        if rank_of_y == rank_of_x:
          // RANK IS NOT A VALUE. IT IS A RANK
          rank[parent_of_x] += 1

```

## Union by compression
```
function init(n):
    parent[1...n] = 1...n
    
    
function find(n):
    // Find the parent of n
    
    if parent[x] != x then
        // If parent of x is not x then update the parent of x to the very top.
        parent[x] = find(parent[x])
        
    // Otherwise parent[x] == x then obviously x is a parent
    
    return parent[x] // Simply return parent of x which contain the true parent.
   
 
function union(x, y):
    // Same deal as normal union.
    parent_of_x = find(x)
    parent_of_y = find(y)
    parent[parent_of_x] = parent_of_y

```
