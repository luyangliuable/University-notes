import sys
import heapq
import math
sys.path.append("/Users/rubber/University-notes/FIT2004/directed-graph/")

import directed_graph as dg

dict = {"p": 0, "q": 1, "r": 2, "s": 3, "t": 4, "u": 5, "v": 6, "w": 7, "x": 8, "y": 9, "z": 10}
# matrix = [[None, None, None, None, None, None, None, None, None, None],
#           [5, None, None, None, None, None, None, None, None, None],
#           [4, None, None, None, None, None, None, None, None, None],
#           [None, None, None, None, None, None, None, None, None, None],
#           [None, None, None, 1, None]]

graph = dg.adjacency_matrix(11)
graph.set_weight(dict['q'], dict['p'], 5)
graph.set_weight(dict['t'], dict['q'], 12)
graph.set_weight(dict['w'], dict['t'], 14)
graph.set_weight(dict['s'], dict['w'], 18)
graph.set_weight(dict['z'], dict['p'], 18)
graph.set_weight(dict['v'], dict['z'], 18)
graph.set_weight(dict['y'], dict['v'], 18)
graph.set_weight(dict['z'], dict['q'], 1)
graph.set_weight(dict['z'], dict['t'], 9)
graph.set_weight(dict['v'], dict['t'], 6)
graph.set_weight(dict['v'], dict['w'], 3)
graph.set_weight(dict['y'], dict['w'], 14)
graph.set_weight(dict['s'], dict['y'], 3)
graph.set_weight(dict['r'], dict['p'], 4)
graph.set_weight(dict['z'], dict['r'], 2)
graph.set_weight(dict['u'], dict['z'], 4)
graph.set_weight(dict['v'], dict['u'], 5)
graph.set_weight(dict['x'], dict['v'], 5)
graph.set_weight(dict['y'], dict['x'], 5)
graph.set_weight(dict['u'], dict['r'], 11)
graph.set_weight(dict['x'], dict['u'], 11)


print(graph.get_matrix())

# functionDIJKSTRA(G=(V,E),s) dist [1..n ] = ∞
# pred[1..n ] = 0
# dist[s]=0
# Q = priority_queue(V [1..n], key(v) = dist[v]) while Q is not empty do
# u = Q.pop_min()
# for each edge e that is adjacent to u do
# // Priority queue keys must be updated if relax improves a distance estimate!
# RELAX(e)
# return dist[1..n], pred[1..n]

def relax(M: list[list[int]], u, v, dist: list[int], pred: list[int], Q: list):
    if dist[v] > dist[u] + M.get_matrix()[u][v]:
        dist[v] = dist[u] + M.get_matrix()[u][v]
        print("before", Q, "changing")
        for i in range(len(Q)):
            if Q[i][1] == v:
                Q[i][0] = dist[v]

        pred[v] = u


def dijkstra(M: list[list[int]], s: int) -> list:
    dist = [math.inf]*len(M)
    pred = [0]*len(M)
    dist[s] = 0
    Q = [[dist[i], i] for i in range(len(M))]
    Q.sort()

    while len(Q) > 0:
        u = heapq.heappop(Q)[1]
        for v in range(len( M.get_matrix()[u] )):
            if M.get_matrix()[v][u] != None:
                relax(M, v, u, dist, pred, Q)
    return dist

print(dijkstra(graph, dict['s']))
