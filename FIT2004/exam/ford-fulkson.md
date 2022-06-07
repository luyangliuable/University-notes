# Ford Fulkerson
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Ford Fulkerson](#ford-fulkerson)
    - [Pseudocode](#pseudocode)
    - [Time complexity](#time-complexity)

<!-- markdown-toc end -->

## Pseudocode

```

function max_flow(G=(V,E))
  maximum_flow = 0
  augment = 1

  while augment is not 0 do
      visited[1...n] = False
      augment = dfs(s, t, inf)
      maximum_flow += augment
    
  return maximum_flow
   
    
function dfs(u, t, bottleneck)
    if u == t:
        // Found an augmenting path
        return bottleneck
        
    visited[u] = True
        
    for each edge e=(u, v) adjacent to u do
        residual = e.capacity - e.flow
        if not visted[v]:
          augment = dfs(v, t, min(bottleneck, residual))
          if augment > 0:
            // If there is an augmenting path detected
            e.flow += augment
            e.reverse.flow -= augment
          
          return augment
        
    return 0
```

## Time complexity
O(|E|*max_flow) where |E| is the total number of edges in the graph and max_flow is the maximum amount of flow because each augmenting path increase flow by at least 1.

