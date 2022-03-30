import sys
from heapq import heappush, heappop
sys.path.append("/Users/rubber/University-notes/FIT2004/directed-graph/")

import undirected_graph
graph = undirected_graph.adjacency_matrix(5)

graph.define_matrix([[None, 1, 1, None, None, None, None, None], [1, None, None, None, 1, 1, None, None], [1, None, None, 1, None, None, None, None], [None, None, 1, None, None, None, None, None], [None, None, None, None, None, None, None, 1], [None, 1, None, None, None, None, 1, None], [None, None, None, None, 1, 1, None, 1], [None, None, None, None, 1, None, 1, None]])


def bfs(M, s: int) -> None:
    visited = [False]*len(M)
    visited[s] = True
    queue = []
    # heappush(queue, (s)) Use queue instead of heap
    queue.append(s)
    while(len(queue) > 0):
        u = queue.pop(0)
        for v in range(len(M.get_matrix()[u])):
            print(queue)
            print(visited)
            if not visited[v]:
                visited[v] = True
                heappush(queue, v)

bfs(graph, 0)
