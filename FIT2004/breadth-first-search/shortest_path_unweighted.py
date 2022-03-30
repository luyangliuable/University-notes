import sys
import math
from heapq import heappush, heappop
sys.path.append("/Users/rubber/University-notes/FIT2004/directed-graph/")
sys.path.append("/Users/rubber/University-notes/FIT2004/")
import undirected_graph
import graphs

graph = graphs.graph2

print("length of the graph is", len(graph))

def bfs(M: list[list[int]], s):
    dist = [math.inf]*len(M)
    pred = [None]*len(M)
    queue = []
    queue.append(s)
    dist[s] = 0
    # heappush(queue, (s)) Use queue instead of heap
    while(len(queue) > 0):
        u = queue.pop(0)
        # print(queue)
        for v in range(len(M.get_matrix()[u])):
            # print("dist v is", dist[v])
            # print("dist u is", dist[u])
            # print(dist)
            if dist[v] == math.inf and M.get_matrix()[u][v] != None:
                pred[v] = u
                dist[v] = dist[u] + 1
                queue.append(v)

    return [dist, pred]

def reconstruct_shortest_path(s: int, u: int, pred: list[int]):
    assert u > s, "starting point must be smaller than end in undirected graph"
    path = [u]
    while u != s:
        if u is not None:
            path.append(pred[u])
            u = pred[u]
            print("u is", u)
    path.reverse()  # Reverse the path to show in the correct sequence
    return path


def find_shortest_path(M: list[list[int]], s: int, u: int) -> list[int]:
    [_, pred] = bfs(graph, s)
    res = reconstruct_shortest_path(s, u, pred)

    return res

# [dist, pred] = bfs(graph, 0)
# print(dist, pred)
# print("The shortest path is:", reconstruct_shortest_path(4, 3, pred))
print("The shortest path is:", find_shortest_path(graph, 0, 2))
