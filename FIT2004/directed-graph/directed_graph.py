class adjacency_matrix:
    """
    This class represents a an graph in the form of adjacency matrix

    author: Luyang Liu
    Copyright: 2010 Luyang Liu
    """
    def __init__(self, n: int) -> None:
        self.vertices = n
        self.matrix = []
        for i in range(n):
            default_weight = None
            self.matrix = self.matrix + [[default_weight]*(n)]


    def set_weight(self, first_node: int, second_node: int, weight: int) -> None:
        if first_node != second_node:
            self.matrix[first_node][second_node] = weight


    def set_matrix(self, M: list[list[int]]):
        self.matrix = M


    def get_weight(self, first_node: int, second_node: int) -> int:
        return self.matrix[first_node][second_node]


    def get_vertices(self) -> int:
        return self.vertices


    def __len__(self):
        return len(self.matrix)


    def get_matrix(self) -> list[list[int]]:
        return self.matrix


class adjacency_list:
    """
    This class represents a an graph in the form of adjacency list

    author: Luyang Liu
    Copyright: 2010 Luyang Liu
    """
    def __init__(self, n: int) -> None:
        self.vertices = n
        self.matrix = []
        for i in range(n):
            default_weight = None
            self.matrix = self.matrix + [[]]


    def set_weight(self, first_node: int, second_node: int, weight: int):
        if first_node != second_node:
            already_exist = False
            for i in range(len(self.matrix[first_node])):
                if self.matrix[first_node][i][0] == second_node:
                    self.matrix[first_node][i][1] = weight
                    already_exist = True
                    break
            if not already_exist:
                self.matrix[first_node] = self.matrix[first_node] + [[second_node, weight]]

    def get_weight(self, first_node: int, second_node: int) -> int:
        for i in range(len(self.matrix[first_node])):
            if self.matrix[first_node][i][0] == second_node:
                return self.matrix[first_node][i][1]

        return None


    def get_vertices(self) -> int:
        return self.vertices


    def get_matrix(self) -> list[list[int]]:
        return self.matrix
