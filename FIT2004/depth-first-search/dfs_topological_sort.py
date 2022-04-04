import sys
sys.path.append("/Users/rubber/University-notes/FIT2004/directed-graph/")

import directed_graph as dg

matrix = [[None, 1, None, None, 1],
          [None, None, 1, 1, 1],
          [None, None, None, None, None],
          [None, None, 1, None, None],
          [None, None, None, 1, None]]
graph = dg.adjacency_matrix(5)
graph.set_matrix(matrix)

###############################################################################
#                          Topological sort using dfs                         #
###############################################################################
def dfs_topological_sort(M: list[list[int]]) -> list[int]:
    order = []
    visited = [False]*len(M)

    for v in range(len(M.get_matrix())): # For each index in each column of matrix
        if not visited[v]:
            dfs(M, v, visited, order)

    order.reverse()
    return order


###############################################################################
#                              Depth first search                             #
###############################################################################
def dfs(M: list[list[int]], u, visited: list[bool], order: list[int]) -> list[int]:
    visited[u] = True

    for v in range(len(M.get_matrix()[u])): # For each index in each row of matrix
        if M.get_matrix()[u][v] != None: # If the value in the row is not None
            if not visited[v]:
                dfs(M, v, visited, order)
    order.append(u)

    return order


print("Result of the topological sort is ", dfs_topological_sort(graph))

