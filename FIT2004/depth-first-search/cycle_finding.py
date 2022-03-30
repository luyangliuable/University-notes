import sys

sys.path.append("/Users/rubber/University-notes/FIT2004/directed-graph/")

import undirected_graph
graph = undirected_graph.adjacency_matrix(5)

graph.define_matrix([[None, 1, 1, None, None, None, None, None], [1, None, None, None, 1, 1, None, None], [1, None, None, 1, None, None, None, None], [None, None, 1, None, None, None, None, None], [None, None, None, None, None, None, None, 1], [None, 1, None, None, None, None, 1, None], [None, None, None, None, 1, 1, None, 1], [None, None, None, None, 1, None, 1, None]])



def dfs(M: undirected_graph.adjacency_matrix, u: int, p: int, visited: list[bool]) -> bool:
    # print("M is currently at", M.get_matrix()[u])
    # print("currently visited are", visited)
    # assert u != None, "u cannot be none"
    visited[u] = True
    for v in range( len(M.get_matrix()[u]) ):
        if M.get_matrix()[u][v] != None: # Adjacent only
            if visited[v] and v != p:
                return True
            elif v != p and dfs(M, v, u, visited) == True:
                return True
    return False

def has_cycle(M: list[list[int]]) -> bool:
    visited = [False]*len(M)
    for i in range(len(M)):
        if not visited[i] and dfs(graph, i, None, visited):
            return True
    return False

print("The graph", str( graph.get_matrix() ), "has cycle is", has_cycle(graph))
