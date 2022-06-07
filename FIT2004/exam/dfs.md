# Depth first search

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Breadth first search](#breadth-first-search)

<!-- markdown-toc end -->

## Pseudocode
```

function start(G=(V,E))
    visited[1..|V|] = False

    for i in 1 to |V|:
        if not visited[i]:
            dfs(G=(V,E), i, visited)

function dfs(G=(V,E), s, visited)
    visited[s] = True
    for each edge e=(u, v) adjacent to s do
        if not visted[v] then
            dfs(G=(V,E), v, visited)
```

## Time complexity
* O(|V| + |E|) where |V| is the number of vertices and |E| is the number of edges. This is because it examines every edge at least once for DAG and it does not examine visited vertices.
