# type1
# input1 = [10, 20, 30, 40, 50]
# input2 = [60, 70, 80, 90, 100]


# def swap(input1, input2):
#     output = []
#     output.append(input2[:2])
#     output.append(input1[2:])
#     return output


# print(swap(input1, input2))
# print(swap(input2, input1))

# type2
# input1 = [10, 20, 30, 40, 50]
# input2 = [60, 70, 80, 90, 100]


# def swap(input1, input2):
#     output = []
#     output.append(input1[:2])
#     output.append([input2[2]])
#     output.append(input1[3:])
#     return output


# print(swap(input1, input2))
# print(swap(input2, input1))

# type3
input1 = [10, 20, 30, 40, 50]
input2 = [60, 70, 80, 90, 100]


def swap(input1, input2):
    output = []
    output.append(input1[0])
    output.append(input2[1:len(input1)-1])
    output.append(input1[len(input1)-1])
    return output


print(swap(input1, input2))
print(swap(input2, input1))
