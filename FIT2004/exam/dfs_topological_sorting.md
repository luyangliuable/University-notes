# DFS Topological sorting
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [DFS Topological sorting](#dfs-topological-sorting)

<!-- markdown-toc end -->

## Pseudocode


```
function dfs_topological_sort(G=(V,E))
    visited[1...|V|] = False
    order = []
    for u in every vertex do:
        if not visited[u] then:
          dfs(u)
        
    return reverse( order )

function dfs(G=(V,E))
    visited[u] = False
    for every vertex v adjacent to u:
      if not visited[v] then:
            dfs(v)
            
    order.append(u)
```
