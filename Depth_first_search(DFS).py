# given any non-cyclical graph, get all paths from a node to the terminating nodes
# can be implemented via recursion as well as using Stack data structure

# using node class to build the graph

class Node:

    def __init__(self,name = None, value=None, leaves = None):
        self.name = name
        self.value = value
        self.leaves = leaves


def DFS_recursive(vertex):
    
    paths = [vertex.name]
    explored = [vertex.name]
    if vertex.leaves is None:
        return vertex.name
    for each in vertex.leaves:
        if each.name not in explored:
            explored.append(each.name)
            paths.append(DFS_recursive(each))
            
    return paths

def DFS_helper(vertex):
    if vertex.leaves is None:
        return vertex.name
    for each in vertex.leaves:
        DFS_helper(each)


A = Node(name="A")
B = Node(name="B")
C = Node(name="C")
D=Node(name='D')
E = Node(name = 'E')
F = Node(name ='F')
A.leaves = [B,C]
B.leaves=[D,E]
C.leaves = [D]
D.leaves = [F]
E.leaves = [F]


print(DFS_recursive(A))

