parent = [1,2,2,4,2,4]

def find(x, parent: list[int]):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)

    return parent[x]

parent_of_element_to_find = 0

print("The parent of", parent_of_element_to_find, "is", find(parent_of_element_to_find, parent))
