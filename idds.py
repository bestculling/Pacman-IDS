def iddfs(start, goal):
    for depth in range(0, max_depth):
        found = dls(start, goal, depth)
        if found != None:
            return found
    return None

def dls(node, goal, depth):
    if depth == 0 and node == goal:
        return goal
    elif depth > 0:
        for child in children_of(node):
            found = dls(child, goal, depth-1)
            if found != None:
                return found
    return None

def children_of(node):
    # implement this function to return the children of a given node in the search tree
    pass

start = 0
goal = 2
max_depth = 3
print(iddfs(start, goal))