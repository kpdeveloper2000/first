# graph input
input = {"S": ["A", "B"], "A": ["C", "D"],
         "B": ["E", "F"], "C": [], "D": [], "E": ["H"], "F": ["I", "G"], "G": [], "H": [], "I": []}
# heruistic input
heuristic = {"S": 13, "A": 12, "B": 4, "C": 7, "D": 3,
             "E": 8, "F": 2, "H": 4, "I": 9,  "G": 0}

# function for greedysearch


def greedySearch(list, start, goal, cost=100):
    # initializing the empty path
    path = []
    # initializing total path as 0
    totalPath = 0
    # loop till goal is not found in the path
    while goal not in path:
        # condition that specifies if start is not in the path to append the start in the path
        if start not in path:
            path.append(start)
        # looping through the neighbour of starting node
        for i in list[start]:
            # condition to check whether the heruistic[i] is less then cost specified or not and if it is satisfied assiging the heruistic[i] as cost and neighbouring node as the start
            if heuristic[i] < cost:
                cost = heuristic[i]
                start = i
        # finding the totalPath by adding totalPath and cost
        totalPath = totalPath + cost
    # returning the path and totalPath travelled
    return path, totalPath


# calling the function greedysearch and assiging it to the varaiable result
result = greedySearch(input, 'S', 'G')
print('Greedy Best First Search')
print(result)
