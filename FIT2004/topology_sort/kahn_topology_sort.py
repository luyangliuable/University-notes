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

def kahn_topological_sort(M: list[list[int]]) -> list[int]:
    order = []
    degrees = [0]*len(M)
    ready = []

    for i in range(len(M)):
        for j in range(len(M.get_matrix()[i])):
            if M.get_matrix()[i][j] == 1:
                degrees[j] += 1

    for i in range(len(degrees)):
        if degrees[i] == 0:
            ready.append(i)

    while len( ready ) != 0:
        u = ready.pop(0)
        order.append(u)
        # for v in range(len(M.get_matrix()[u])):
        #     print(v)


        for v in range(len(M.get_matrix()[u])):
            # print(len(M.get_matrix()[u]))
            if degrees[v] != 0 and M.get_matrix()[u][v] != None:
                # print(degrees, "has edges left")
                ready.append(v)
                degrees[v] -= 1
    return order

print("The sorted order is", kahn_topological_sort(graph))
