# Week 5 Studio

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Week 5 Studio](#week-5-studio)
- [Problem 5: Two colour able](#problem-5-two-colour-able)

<!-- markdown-toc end -->

 # Problem 4

```
function reachable(G=(V,E), s)
    visited[1...|V|] = False
    reachable = []
    dfs(G=(V,E), s, visited, reachable)
    
    return reachable
    
    
function dfs(G=(V,E), s)
    visited[s] = True
    
    for every edge e = (u, v) adjacent to u do
        if visited[v] = False:
            dfs(G=(V,E), v)
            
    reachable.append(s)
```


# Problem 5: Two colour able

```
function two_colorable(G=(V,E))
    colour[1...|V|] = None
    queue = Queue()
    queue.append(vertices without incoming edges)
    
    while queue is not empty do
        u = queue.pop()
        
        for every vertex v adjacent to u do
            if colour[v] is not None:
              if colour[v] = not colour[u] then
                  return false
            else:
                colour[v] = not colour[u]
                
    return True
```


```
function two_colourable(G=V(V,E))
    colour[1..|V|] = null
    
    for each vertex u = 1 to |V| do
        if colour[u] == null then
          if dfs(G=V(V,E), u, colour) == False then
              return False
        
    return True
    
function dfs(G=V(V,E), s, colour)

    for each vertex v adjacent to u do:
        if colour[v] == null:
            colour[v] = not colour[s]
            if dfs(v) == False then
                return False
        else if colour[v] == colour[s] then
              return False
```

## Problem 6 Cycle finding

### Why the algorithm given for finding cycles in an undirected graph does not work when applied to a directed graph
* By definition a cycle is a when a path leads back to the starting point of traversal. 
* In a DAG, this can be avoided by leading to a vertex without any outgoing edges that could lead to the original source vertex.
* When using dfs to check for cycles, once it realised that it is going to traverse to a visited edge then it determines there is a cycle. For undirected this is always the case because the next vertex in the edge always can connect back to the visited vertex u in e=(u, v)

### DFS algorithm to find cycles
```
function find_cycles(G=(V,E))
    visited[1..|V|] = False
      
    for each vertex u in 1 .. |V| do
        if not visited[u] and dfs(G=(V,E), s) then
            return True
            
    return False
          
function dfs(G=(V,E), u)
    visited[u] = True
    
    for every vertex v adjacent to u do
        if visited[v] == True then 
            return True
        else if dfs(G=(V,E), v) == True then
            return True
            
    visited[u] = False // FInished mark this as not visited
    
```

## Problem 7: Shorted cycle in an unweighted directed graph
```
function shortest_cycles(G=(V,E))
    visited[1..|V|] = False
      
    min_cycle = inf

    for each vertex u in 1 .. |V| do
        if not visited[u] then 
            min_cycle = min(inf, dfs(G=(V,E))
            
    return min_cycle
          
function dfs(G=(V,E), u, numcycle, chain)
    visited[u] = True
    
    chain.append(u)
    numcycle += 1

    for every vertex v adjacent to u do
        if visited[v] == True then 
            return numcycle
        else if dfs(G=(V,E), v, numcycle, chain) == True then
            return numycle
            
    return inf
            
    visited[u] = False // FInished mark this as not visited
```

## Problem 8: Multiple source vertices on unweighted graph

```
function multi_source_shortest_path(G=(V, E), S)
    dist[1...n] = inf
    pred[1...n] - null
    
    queue = Queue()
    for each source vertex s in S do
      queue.append(s)
    
    while queue is not empty do:
        u = queue.pop()
        for every vertex v adjacent to u do
            if dist[v] == inf then
                dist[v] = dist[u] + 1
                pred[v] = u
                queue..push(v)
              
    return distance
              
```

## Problem 9: Number of valid two colouring

* If two colouring is possible in the graph then the total number of possible colouring is 2^(number of connected components)

```
function valid_two_colourings(G=(V,E))
    colour[1...n] = null
    
    valid = 0
    for every vertex u in 1...n do:
        if colour[u] == null then
            search = dfs(u, 1, 0)
            if search == False then
                return False
            else
                valid = max(search , valid)
                
                
    return Valid
    
function dfs(s, c, counter)
    colour[s] = c
    
    max_counter = 0
    for every vertex v adjacent to u do:
        if colour[v] == null:
            search = dfs(v, not colour[s]
            if search is not False then
              max_counter = max(search, counter + 1), max_counter)
              
            else if search == False:
              return False
      else if colour[v] == colour[u]:
          return False 
            
    return max_counter
```

## Problem 10: Count the number of connected components that form a cycle


```
function count_cycle_components(G=(V,E))
    visited[1..n] = False
    
    cycle_components = 0

    for every vertex u in 1...n do:
      if dfs(v) then
        cycle_components += 1

        
function dfs(u, counter)
    visited[u] = True

    for every vertex v adjacent to u do
      if visited[v] = False then
        return dfs(v)

      else if visited[v] then
        return True
          
    visited[u] = False // Mark this mark as False for reuse later.

    return False
```


