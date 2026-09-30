import cv2 
import numpy as np
import matplotlib.pyplot as plt

img1= cv2.imread(r"C:\Syeda_Nazish\practicle\DIP\ken-cheung.jpg")
img2= cv2.imread(r"C:\Syeda_Nazish\practicle\NN_PRACTICLE\color_back.jpg")

if img1 is None or img2 is None:
    print("error : image not found!")
    exit()
img2=cv2.resize(img2,(img1.shape[1],img1.shape[0]))
add=cv2.add(img1,img2)
sub=cv2.subtract(img1,img2)

logical_and=cv2.bitwise_and(img1,img2)
logical_OR=cv2.bitwise_or(img1,img2)
logical_NOT=cv2.bitwise_not(img1,img2)
logical_xor=cv2.bitwise_xor(img1,img2)

plt.subplot(2,4,1)
plt.imshow(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
plt.title("Image 1")
plt.axis("off")

plt.subplot(2,4,2)
plt.imshow(cv2.cvtColor(img2,cv2.COLOR_BGR2RGB))
plt.title("Image 2")
plt.axis("off")

plt.subplot(2,4,3)
plt.imshow(cv2.cvtColor(add,cv2.COLOR_BGR2RGB))
plt.title("Addition")
plt.axis("off")

plt.subplot(2,4,4)
plt.imshow(cv2.cvtColor(sub,cv2.COLOR_BGR2RGB))
plt.title("Subtract")
plt.axis("off")

plt.subplot(2,4,5)
plt.imshow(cv2.cvtColor(logical_and,cv2.COLOR_BGR2RGB))
plt.title("ADD")
plt.axis("off")

plt.subplot(2,4,6)
plt.imshow(cv2.cvtColor(logical_OR,cv2.COLOR_BGR2RGB))
plt.title("OR")
plt.axis("off")

plt.subplot(2,4,7)
plt.imshow(cv2.cvtColor(logical_NOT,cv2.COLOR_BGR2RGB))
plt.title("NOT- Image 1")
plt.axis("off")

plt.subplot(2,4,8)
plt.imshow(cv2.cvtColor(logical_xor,cv2.COLOR_BGR2RGB))
plt.title("XOR")
plt.axis("off")

plt.tight_layout()
plt.show()