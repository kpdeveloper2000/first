def rel(y):
    if y > 0:
        return 1
    elif y < 0:
        return -1
    else:
        return 0


# initializing weight to 0
w = [0, 0]
# initializing bias to 0
b = 0
# initializing learning rate to 1
alpha = 1

# input trainings
x1 = [-1, -1, 1, 1]
x2 = [-1, 1, 1, 1]

# targeted output
t = [1, -1, 1, 1]
print("x1\tx2\tt\tyin\ty\tdw1\tdw2\tdb\tw1\tw2\tb")
for i in range(len(x1)):

    # computing output response as Yin = b +sum(xiwi)
    yin = b+(x1[i]*w[0]+x2[i]*w[1])
    y = rel(yin)
    if y is not t[i]:
        dw1 = alpha*t[i]*x1[i]
        dw2 = alpha*t[i]*x2[i]
        db = alpha*t[i]
    else:
        dw1, dw2, b = 0, 0, 0

    w[0] = w[0] + dw1
    w[1] = w[1] + dw2
    b += db
    print(x1[i],"\t",x2[i],'\t',t[i],'\t', yin,'\t', y,'\t',dw1,'\t',dw2,'\t',db,'\t',w[0],'\t',w[1],'\t',b)
