from math import e


def function_(x):  # activation function
    return 1 / (1 + e ** (-1 * x))


# initializing weights
alpha = 0.3
w = [1, 1, 0]
w0 = -1
v = [[1, 1, 0], [1, 1, 4], [2, 3, 2]]
v0 = [0, 0, 1]
x = [0.5, 0.3, 0.2]
t = 0.9  # setting target output = 0.9
z = []
for i in range(3):
    zin = v0[i] + x[1] * v[i][0] + x[1] * v[i][1] + x[1] * v[i][2]
    z.append(function_(zin))
# finding feed forward stage
Y = w0 + z[0] * w[0] + z[1] * w[1] + z[2] * w[2]
Y = function_(Y)
# finding back propagation of error
del_k = (t * Y) * (function_(Y) * (1 - function_(Y)))
del_inj = []
for i in range(3):
    val = del_k * w[i]
    del_inj.append(val)
del_j = []
for i in range(3):
    val = del_inj[i] * (function_(z[i]) * (1 - function_(z[i])))
    del_j.append(val)

# updating weight and bias
for i in range(3):
    for j in range(3):
        v[i][j] = v[i][j] + alpha * del_j[j]
for i in range(3):
    v0[i] = v0[i] + alpha * del_j[i]
for i in range(3):
    w[i] = w[i] + alpha * del_k * z[i]
w0 = w0 + alpha * del_k

# displaying the data
print("After all operation the values are:")
print("v: ")
for i in v:
    for j in i:
        print("\t", j, "\t", end="")
    print("")
print("v0 = ", v0)
print("w = ", w)
print("w0 = ", w0)
