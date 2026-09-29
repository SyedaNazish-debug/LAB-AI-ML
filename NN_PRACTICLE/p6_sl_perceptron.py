X=[[0,0],
   [1,0],
   [0,1],
   [1,1]]
Y=[1,1,1,0]
w1=0
w2=0

eta=1
print("Hebbian learning")

for i in range(len(X)):
    x1=X[i][0]
    x2=X[i][1]
    y=Y[i]

    dw1=eta*x1*y
    dw2=eta*x2*y

    w1 = w1 + dw1
    w2 = w2 + dw2

    print("\n Input:",x1, x2)
    print("\n Output:",y)
    print("Change in weights :", dw1 , dw2)
    print("Updated weights:", w1,w2)

print("\n Final weights:", "w1 =",w1, "w2 =",w2)