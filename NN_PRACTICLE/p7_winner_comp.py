import math
X=[[1,1],[1,2],[2,1],[8,8],[9,8],[8,9]]
W=[[1,1],[8,8]]
alpha = 0.5
epochs = 5

for epoch in range(epochs):
    print("\n Epochs", epoch+1)
    for x in X:
        d1=math.sqrt(
            (x[0]-W[1][0])**2+(x[1]-W[1][1])**2
       )
        d2=math.sqrt(
                    (x[0]-W[1][0])**2+(x[1]-W[1][1])**2
               )
        if d1 <  d2:
            winner=0
        else:
            winner =1

        for j in range(2):
            W[winner][j]=(
                W[winner][j]+alpha*(x[j]-W[winner][j])
            )
        print(
            "input=",x,
            "winner=neuron",winner+1
        )
    print("\n Final weights:")
    for i in range(len(W)):
            print("neuron",i+1,":",W[i])
