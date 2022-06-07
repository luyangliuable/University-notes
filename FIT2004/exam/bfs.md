# Breadth first search

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Breadth first search](#breadth-first-search)

<!-- markdown-toc end -->

## Pseudocode

* G=(V,E) means a graph with list of vertices and edges.
* e=(u, v) means an edge with 2 vertices u and v.

```
function bfs(G=(V,E), s, item)
    visited[1...n] = False
    queue = Queue() // When reference to objects (e.g. bst, queue using Bst() and Queue())
    
    queue.push(s) // Queue is FILO
    
    while queue is not empty:
        u = queue.pop()
        for each edge e=(u,v) adjacent to u do
            if not visited[v] then
                if v == item:
                    // find the same item
                    return v
                queue.push(v) 
                
    // item not in graph
    return null
        

```

## Time complexity
### Worst case 
* O(|V| + |E|) because every edge must be traversed and vertices checked/added to queue. |V| is the number of vertices and |E| is the number of edges.


## Auxiliary Space complexity
* O(|V|) where |V| is the number of vertices because the min_heap could have all vertices inside.
