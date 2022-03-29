import sys
sys.path.append("/Users/rubber/University-notes/FIT2004/directed-graph/")
import undirected_graph

graph = undirected_graph.adjacency_matrix(5)

graph.define_matrix([[None, 1, 1, None, None, None, None, None], [1, None, None, None, 1, 1, None, None], [1, None, None, 1, None, None, None, None], [None, None, 1, None, None, None, None, None], [None, None, None, None, None, None, None, 1], [None, 1, None, None, None, None, 1, None], [None, None, None, None, 1, 1, None, 1], [None, None, None, None, 1, None, 1, None]])

for i in graph.get_matrix():
    if len(i) != 8:
        print("wrong!")
    else:
        print("correct")
if len( graph.get_matrix() ) != 8:
    print("wrong")

def traverse(M: list[list[int]]):
    visited = [False]*len(M)

    for i in range(len(M)):
        if visited[i] == False:
            print(i, "is not yet visited")
            dfs(M, i, visited)

def dfs(M: undirected_graph.adjacency_matrix, u: int, visited: list[bool]) -> None:
    visited[u] = True
    print("M is currently at", M.get_matrix()[u])
    print("currently visited are", visited)
    for item in M.get_matrix()[u]:
        if not visited[u]:
            dfs(M, item, visited)

traverse(graph)
