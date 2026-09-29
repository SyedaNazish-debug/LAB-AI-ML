import cv2 
import numpy as np
import matplotlib.pyplot as plt

img1=cv2.imread("img.jpg")
img2=cv2.imread("color_back.jpg")

if img1 is None or img2 is None:
    print("images not found")
    exit()

img2=cv2.resize(img2,(img1.shape[1],img1.shape[0]))

add= cv2.add(img1,img2)
sub=cv2.subtract(img1,img2)
logic_add=cv2.bitwise_and(img1,img2)
logic_or=cv2.bitwise_or(img1,img2)
logic_not=cv2.bitwise_not(img1)

plt.figure(figsize=(12,8))

plt.subplot(2,3,1)
plt.imshow(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
plt.title("Image 1")
plt.axis("off")

plt.subplot(2,3,2)
plt.imshow(cv2.cvtColor(img2,cv2.COLOR_BGR2RGB))
plt.title("Image 2")
plt.axis("off")

plt.subplot(2,3,3)
plt.imshow(cv2.cvtColor(add,cv2.COLOR_BGR2RGB))
plt.title("ADD")
plt.axis("off")

plt.subplot(2,3,4)
plt.imshow(cv2.cvtColor(sub,cv2.COLOR_BGR2RGB))
plt.title("SUB")
plt.axis("off")

plt.subplot(2,3,5)
plt.imshow(cv2.cvtColor(logic_add,cv2.COLOR_BGR2RGB))
plt.title("Logical AND")
plt.axis("off")

plt.subplot(2,3,6)
plt.imshow(cv2.cvtColor(logic_or,cv2.COLOR_BGR2RGB))
plt.title("logical OR")
plt.axis("off")

plt.tight_layout()
plt.show()


plt.imshow(cv2.cvtColor(logic_not,cv2.COLOR_BGR2RGB))
plt.title("logical NOT ")
plt.show()
