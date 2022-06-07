# Bellman ford algorithm


## Pseudocode

```
function bellman_ford(G=(V,E), s)

distance[1...n] = inf
pred[1...n] = null

dist[s] = 0

for vertex u in 1...n-1:
    for every vertex v adjacent to u:
        distance[v] = min(distnance[v], distance[u] + w(u, v))

        if distance[v] > distance[u] + w(u, v) then
            pred[v] = u
        
return dist[1...n], pred[1...n]
```

## Cycle finding using bellman ford
```
function bellman_ford(G=(V,E), s)

distance[1...n] = inf
pred[1...n] = null

dist[s] = 0

for vertex u in 1...n-1:
    for every vertex v adjacent to u:
        distance[v] = min(distnance[v], distance[u] + w(u, v))

        if distance[v] > distance[u] + w(u, v) then
            pred[v] = u
        
return dist[1...n], pred[1...n]
```

```
function detect_cycle(G=(V,E), s)
    distance, pred = bellman_ford(G=(V,E), s)

    for every edge e = (u, v) adjacent to u:
        if dist[v] > dist[u] = w(u, v):
            // After bellman ford, if additional relexation results in smaller distance this means that there is a neg. cycle. Mark dist[v] and -inf
            dist[v] = -inf
```


## Time complexity
O((|V|-1)|E|) or O(|V||E|) worst case


