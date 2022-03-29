import sys
import undirected_graph

sys.path.append("/Users/rubber/University-notes/FIT2004/directed-graph/")

test_matrix_graph = undirected_graph.adjacency_matrix(5)

test_matrix_graph.set_weight(0, 1, 1)
test_matrix_graph.set_weight(1, 2, 1)
test_matrix_graph.set_weight(1, 3, 1)
test_matrix_graph.set_weight(4, 0, 1)
test_matrix_graph.set_weight(2, 3, 1)
test_matrix_graph.set_weight(3, 4, 1)
test_matrix_graph.set_weight(4, 1, 1)
test_matrix_graph.get_matrix()[0][1] = 100
# print(test_matrix_graph.get_matrix())

test_list_graph = undirected_graph.adjacency_list(5)

test_list_graph.set_weight(0, 1, 1)
test_list_graph.set_weight(0, 4, 1)
test_list_graph.set_weight(4, 1, 1)
test_list_graph.set_weight(1, 3, 1)
test_list_graph.set_weight(2, 3, 1)
test_list_graph.set_weight(3, 4, 1)
test_list_graph.set_weight(1, 2, 1)
# test_list_graph.get_matrix()[0][1] = 100
print(test_list_graph.get_matrix())
