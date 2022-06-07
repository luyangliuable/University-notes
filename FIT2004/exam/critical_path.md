# Critical path problem
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Critical path problem](#critical-path-problem)
    - [Bottom up](#bottom-up)
        - [Pseudocode](#pseudocode)
    - [Top Down](#top-down)
        - [Pseudocode](#pseudocode-1)

<!-- markdown-toc end -->

## Bottom up
### Pseudocode

```
function critical_path(G=(V, E))
    longest[1...n] = 0
    order = reverse(topology_sort(G))
    
    for each vertex u in order
        for each edge = (u, v) adjacency to u
            longest[u] = max(longest[u], longest[u] + w(u, v))
            
            
    return longest
    
    
function kahn_topological_sort(G=(V,E))
    copy(V,E) = G(V,E)
    order = []
    queue = Queue()
    
    queue.append(all vertex without outgoing edges)
    
    while queue is not empty do
        u = queue.pop()
        order.append(u)
        
        for each edge e=(u,v) adjacent to u do
            copy.remove(u,v)
            if v has no remaining incoming edges then
                // if v has no remaining edges then it is final in topology sort. Otherwise this could mean there  is an edge that could come earlier somewhere.
                queue.append(v)
            
        
    return  order // Don't need to reverse order for kahn
```


## Top Down

### Pseudocode
```
function critical_path(G=(V,E), u)
    if longest[u] == null then // Not yet visited
      longest[u] = 0
      for each edge u = (u, v) adjacenct to u do
            longest[u] = max(longest[u], w(u, v) + critical_path(G(V,E), u))
        
    return longest[u] // return 0 if it has no outgoing edges

```
