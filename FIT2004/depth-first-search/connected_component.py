import sys
import dfs

sys.path.append("/Users/rubber/University-notes/FIT2004/directed-graph/")

import undirected_graph

graph = undirected_graph.adjacency_matrix(5)

graph.define_matrix([[None, 1, 1, None, None, None, None, None], [1, None, None, None, 1, 1, None, None], [1, None, None, 1, None, None, None, None], [None, None, 1, None, None, None, None, None], [None, None, None, None, None, None, None, 1], [None, 1, None, None, None, None, 1, None], [None, None, None, None, 1, 1, None, 1], [None, None, None, None, 1, None, 1, None]])


def connected_component(M: list[list[int]]) -> list:
    component = [None]*len(M)
    num_components = 0
    visited = [False]*len(M)
    for u in range(len(M)):
        if component[u] == None:
            num_components += 1
            dfs(graph, u, component, num_components)

    return [num_components, component]


def dfs(M: undirected_graph.adjacency_matrix, u: int, component: list[int], comp_num: int) -> None:
    component[u] = comp_num
    # print("M is currently at", M.get_matrix()[u])
    # print("currently visited are", visited)
    for item in M.get_matrix()[u]:
        if not component[u]:
            dfs(M, item, component, comp_num)

print("The connected components are", connected_component(graph)[1], "and there are ", connected_component(graph)[0], "components that are connected" )
