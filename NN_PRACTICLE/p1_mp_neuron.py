def mp_neuron(x1,x2):
    w1 = 1
    w2 = 1

    threshold = 2

    summation = (x1*w1)+(x2* w2)

    if summation>=threshold:
        output=1
    else:
        output=0
    return output
inputs=[(0,0),(0,1),(1,0),(1,1)]
print("x1 x2 output")

for x1, x2 in inputs:
    y=mp_neuron(x1,x2,)
    print(x1," ", x2, " ",y)