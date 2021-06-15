# initializing the input graph
input = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}


def dfs(list, node, visited):
    # adding node to the visited if it not present in it
    if node not in visited:
        visited.append(node)
    # looping through the neighbouring nodes
    for i in list[node]:
        # recursively calling the dfs function
        dfs(list, i, visited)
    # returning the visited list created
    return visited


print('Depth first search')
print(dfs(input, '5', []))
