# initializing the empty list of visited nodes
visited = []
# initializing the queue as empty
queue = []
# input for the algorithm
input = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# function bfs that defines how the searching is done


def bfs(visited, list, node):
    # appending node to the queue and visited
    queue.append(node)
    visited.append(node)
    # till the queue is not empty poping its item and traversing through neighbours
    while queue:
        s = queue.pop(0)
        yield s
        for i in list[s]:
            if i not in visited:
                visited.append(i)
                queue.append(i)


# looping to print the value poped from the queue
for i in bfs(visited, input, 'B'):
    print(i, end=' ')
