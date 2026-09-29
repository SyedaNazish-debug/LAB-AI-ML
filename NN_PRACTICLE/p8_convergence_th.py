X=[[0,0],[0,1],[1,0],[1,1]]
T=[0,1,1,1]
w=[0,0]
b=0
eta=1
max_epochs=20

def activation(net):
    if net>=0:
        return 1
    else:
        return 0
for epoch in range (max_epochs):
    errors=0
    for i in range(len(X)):
        net=(
        X[i][0]*w[0]+
        X[i][1]*w[1]+
        b
    )

    y=activation(net)
    error=T[i]-y

    if error !=0:
      w[0]=[0] + eta * error * X[i][0]
      w[1]=w[1] + eta * error * X[1][1]
      b=b+eta*error

    errors+=1
    print("Epochs",epoch+1,
          "error:",errors,
          "weights:",w,
          "bais:",b)
    if errors == 0:
     print("\n Perceptron has converged:")
     break

print("\n final classification:")

for i in range (len(X)):
     net=(
        X[i][0]*w[0]+
        X[i][1]*w[1]+
        b
    )
y=activation(net)

print(
        "input:",X[i],
        "Target:",T[i],
        "Output:",y)