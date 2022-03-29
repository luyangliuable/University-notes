import sys
sys.path.append("/Users/rubber/University-notes/FIT2004/directed-graph/")

import undirected_graph
graph = undirected_graph.adjacency_matrix(5)

graph.define_matrix([[None, 1, 1, None, None, None, None, None], [1, None, None, None, 1, 1, None, None], [1, None, None, 1, None, None, None, None], [None, None, 1, None, None, None, None, None], [None, None, None, None, None, None, None, 1], [None, 1, None, None, None, None, 1, None], [None, None, None, None, 1, 1, None, 1], [None, None, None, None, 1, None, 1, None]])
