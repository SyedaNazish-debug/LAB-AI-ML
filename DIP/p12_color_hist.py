import cv2
import numpy as np
import matplotlib.pyplot as plt

path = r"c:\Syeda_Nazish\practicle\DIP\color_back.jpg"

img = cv2.imread(path)

if img is None:
    print("Image could not be loaded.")
    exit()
print("Image loaded successfully.")
print("Image shape:", img.shape)

img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

red_hist=cv2.calcHist([img_rgb],[2],None,[256],[0,256])
green_hist=cv2.calcHist([img_rgb],[1],None,[256],[0,256])
blue_hist=cv2.calcHist([img_rgb],[0],None,[256],[0,256])

plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(2,2,2)
plt.plot(red_hist,color='r')
plt.title("Red Histogram")
plt.xlabel("pixel intensity value")
plt.ylabel("Number of Pixels")
plt.xlim([0,256])

plt.subplot(2,2,3)
plt.plot(green_hist,color='g')
plt.title("Green Histogram")
plt.xlabel("pixel intensity value")
plt.ylabel("Number of Pixels")
plt.xlim([0,256])

plt.subplot(2,2,4)
plt.plot(blue_hist,color='b')
plt.title("Blue Histogram")
plt.xlabel("pixel intensity value")
plt.ylabel("Number of Pixels")
plt.xlim([0,256])

plt.tight_layout()
plt.show()