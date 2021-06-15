# Input Graph
input = {"S": ["A", "D"], "A": ["S", "B", "C"],
         "B": ["A", "C", "D", "E"], "C": ["A", "B", "G"],
         "D": ["S", "B", "E"], "E": ["B", "D", "G"], "G": ["C", "E"]}
# Input Heiristic
heuristic = {"S": 7, "A": 9, "B": 4, "C": 2, "D": 5, "E": 3, "G": 0}
# Path Cost
pathcost = {"AS": 3, "DS": 4, "AB": 2, "AC": 5, "BD": 1,
            "BC": 2, "BE": 1, "CG": 4, "DE": 5, "EG": 13}
# Initializing Empty Queue
queue = []
# Initializing Cost List
cost = []

# function to determine the path


def PC(path):
    # initializing he as 0
    he = 0
    # looping through heruistic and checking assiging he as sum of he and heriustic[i] if i is in path
    for i in heuristic:
        if i in path:
            he = he + heuristic[i]
    # looping through the path, assiging val1,val2 and sorting them by keeping in array
    for i in range(len(path) - 1):
        val1 = path[i]
        val2 = path[i + 1]
        temp = [val1, val2]
        temp.sort()
        sn = ""
        for j in temp:
            sn = sn + j
        if sn in pathcost:
            he = he + pathcost[sn]
        del sn
        del temp
    return he


def add_path(path):
    temp = []
    # looping through path and appending it on temp
    for i in path:
        temp.append(i)
    # adding items of temp to the queue
    queue.append(temp)


def r(node, trace, goal):
    # checking if goal is not in trace and calling add_path function and adding trace to the cost
    if goal in trace:
        add_path(trace)
        cost.append(PC(trace))
        return
    # if goal is not in trace appending node to the trace
    if node not in trace:
        trace.append(node)
    child = input[node]
    for i in child:
        if i not in trace:
            r(i, trace, goal)
    trace.remove(node)


def A_star_search():
    r("S", [], "G")
    re_p = []
    c = 100
    for i in range(len(queue)):
        print(queue[i], "cost = ", cost[i])
        # if cost[i] is less than c then replacing cost by cost[i]
        if cost[i] < c:
            c = cost[i]
            re_p = queue[i]
    return re_p, c


print("Possible path and cost are: ")
print("\nThe path and cost are returned by A* search as:-\n", A_star_search())
