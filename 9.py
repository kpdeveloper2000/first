import random


def add(list):
    temp = []
    for i in list:
        temp.append(i)
    return temp


# initializing the population
population = [[1, 2, 3, 4], [5, 6, 6, 8], [5, 2, 3, 4], [7, 8, 9, 6]]

# initializing parent1 and parent 2 as empty
parent1, parent2 = [], []
# looping while parent1==parent2 and appending the population in parent1 and parent2
while parent1 == parent2:
    parent1 = population[random.randint(0, 3)]
    parent2 = population[random.randint(0, 3)]
print("First parent = ", parent1)
print("Second parent = ", parent2)
# applying crossover
crossover_point = random.randint(0, len(parent1)-1)
print("cross over point = ", crossover_point)
# initializing chid as empty
child = []
for i in range(crossover_point, len(parent1)):
    temp = parent1[i]
    parent1[i] = parent2[i]
    parent2[i] = temp
    child.append(add(parent1))
    child.append(add(parent2))
    temp = parent1[i]
    parent1[i] = parent2[i]
    parent2[i] = temp
# mutation
for member in child:
    mut_point = random.randint(0, len(member)-1)
    member[mut_point] = int(member[mut_point]/random.randint(1, 3))
# display data
print("Now the added population are: ")
print(child)
