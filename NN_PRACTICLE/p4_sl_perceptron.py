X=[[0,0],
   [0,1],
   [1,0],
   [1,1]]
T=[0,0,0,1]
w1=0
w2=0
b=0

eta=1

for epoch in range(10):
    error_count=0

    for i in range(len(X)):
        x1=X[i][0]
        x2=X[i][1]
        target=T[i]

        net=x1*w1+x2*w2+b

        if net>=1:
            output=1
        else:
            output=0

        error = target-output
        w1=w1+eta*error*x1
        w2=w2+eta*error*x2
        b=b+eta*error

        if error!=0:
            error_count+=1
    if error_count == 0:
        break
print("final weights & bias:",w1, w2 ,b)
print("\n AND gate output:")
for x in X:
    net=x[0]*w1+x[1]*w2+b
    if net>1:
        output=1
    else:
        output=0
    print(x[0],x[1],"=>", output)