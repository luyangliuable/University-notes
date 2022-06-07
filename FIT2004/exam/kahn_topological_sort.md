# Kahn Topological sort
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Kahn Topological sort](#kahn-topological-sort)

<!-- markdown-toc end -->


## Pseudocode

```
function kahn_topological_sort(G=(V,E))
    
    queue[1...q] = vertices with only outgoing edges 
    order[1...-1] = null

    while queue is not empty do
        u = queue.pop()
        order.append(u)
        for every edge e=(u, v) adjacent to u do
            G.remove(e=(u,v))
            if v has no remaining incoming edges then
              queue.push(v)
              
              
    return order
```
