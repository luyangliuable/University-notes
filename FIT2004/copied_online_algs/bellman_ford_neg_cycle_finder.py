# A Python3 program to check if a graph contains negative
# weight cycle using Bellman-Ford algorithm. This program
# works only if all vertices are reachable from a source
# vertex 0.

# a structure to represent a weighted edge in graph
class Edge:

	def __init__(self):
		self.src = 0
		self.dest = 0
		self.weight = 0

# a structure to represent a connected, directed and
# weighted graph
class Graph:

	def __init__(self):

		# V. Number of vertices, E. Number of edges
		self.V = 0
		self.E = 0

		# graph is represented as an array of edges.
		self.edge = None

# Creates a graph with V vertices and E edges
def createGraph(V, E):

	graph = Graph()
	graph.V = V;
	graph.E = E;
	graph.edge =[Edge() for i in range(graph.E)]
	return graph;

# The main function that finds shortest distances
# from src to all other vertices using Bellman-
# Ford algorithm. The function also detects
# negative weight cycle
def isNegCycleBellmanFord(graph, src):

	V = graph.V;
	E = graph.E;
	dist = [1000000 for i in range(V)];
	dist[src] = 0;

	# Step 2: Relax all edges |V| - 1 times.
	# A simple shortest path from src to any
	# other vertex can have at-most |V| - 1
	# edges
	for i in range(1, V):
		for j in range(E):

			u = graph.edge[j].src;
			v = graph.edge[j].dest;
			weight = graph.edge[j].weight;
			if (dist[u] != 1000000 and dist[u] + weight < dist[v]):
				dist[v] = dist[u] + weight;

	# Step 3: check for negative-weight cycles.
	# The above step guarantees shortest distances
	# if graph doesn't contain negative weight cycle.
	# If we get a shorter path, then there
	# is a cycle.
	for i in range(E):

		u = graph.edge[i].src;
		v = graph.edge[i].dest;
		weight = graph.edge[i].weight;
		if (dist[u] != 1000000 and dist[u] + weight < dist[v]):
			return True;

	return False;

# Driver program to test above functions
if __name__=='__main__':

	# Let us create the graph given in above example
	V = 5; # Number of vertices in graph
	E = 8; # Number of edges in graph
	graph = createGraph(V, E);

	# add edge 0-1 (or A-B in above figure)
	graph.edge[0].src = 0;
	graph.edge[0].dest = 1;
	graph.edge[0].weight = -1;

	# add edge 0-2 (or A-C in above figure)
	graph.edge[1].src = 0;
	graph.edge[1].dest = 2;
	graph.edge[1].weight = 4;

	# add edge 1-2 (or B-C in above figure)
	graph.edge[2].src = 1;
	graph.edge[2].dest = 2;
	graph.edge[2].weight = 3;

	# add edge 1-3 (or B-D in above figure)
	graph.edge[3].src = 1;
	graph.edge[3].dest = 3;
	graph.edge[3].weight = 2;

	# add edge 1-4 (or A-E in above figure)
	graph.edge[4].src = 1;
	graph.edge[4].dest = 4;
	graph.edge[4].weight = 2;

	# add edge 3-2 (or D-C in above figure)
	graph.edge[5].src = 3;
	graph.edge[5].dest = 2;
	graph.edge[5].weight = 5;

	# add edge 3-1 (or D-B in above figure)
	graph.edge[6].src = 3;
	graph.edge[6].dest = 1;
	graph.edge[6].weight = 1;

	# add edge 4-3 (or E-D in above figure)
	graph.edge[7].src = 4;
	graph.edge[7].dest = 3;
	graph.edge[7].weight = -3;

	if (isNegCycleBellmanFord(graph, 0)):
		print("Yes")
	else:
		print("No")

		# This code is contributed by pratham76
