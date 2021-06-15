# initializing bias and weight to 0
b = 0
w = [0, 0]

# inputs of trainging vector
x1 = [-1, -1, 1, 1]
x2 = [-1, 1, 1, 1]

# targeted output vector
y = [1, -1, 1, 1]

print('x1\t\tx2\t\ty\t\tw1\t\tw2\t\tb')

for i in range(len(x1)):
    cw1 = x1[i]*y[i]
    cw2 = x2[i]*y[i]
    # applying wi(new) = wi(old) + XiY ( i= 1 to n)
    w[0] = w[0]+cw1
    w[1] = w[1]+cw2
    # applying  b(new) = b(old) + Y
    b += y[i]
    print(x1[i], "\t\t", x2[i], "\t\t", y[i],
          "\t\t", w[0], "\t\t", w[1], "\t\t", b)
