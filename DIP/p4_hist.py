import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("ken-cheung.jpg")

if img is None:
    print("Error:Image not found")
    exit()

img_rgb= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

hist_r=cv2.calcHist([img_rgb],[0],None,[256],[0,256])

hist_g=cv2.calcHist([img_rgb],[1],None,[256],[0,256])

hist_b=cv2.calcHist([img_rgb],[2],None,[256],[0,256])

ycrcb=cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)

ycrcb[:,:,0]=cv2.equalizeHist(ycrcb[:,:,0])

equalized=cv2.cvtColor(ycrcb,cv2.COLOR_BGR2YCrCb)
equalized_rgb=cv2.cvtColor(equalized,cv2.COLOR_BGR2RGB)


plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")


plt.subplot(2,2,2)
plt.imshow(equalized_rgb)
plt.title("Histogram Equalized Image")
plt.axis("off")

plt.subplot(2,2,3)
plt.plot(hist_r, label="Red")
plt.plot(hist_g, label="Green")
plt.plot(hist_b, label="Blue")

plt.title("Original Image Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.legend()

equalized_hist_r=cv2.calcHist(
    [equalized_rgb],[0],None,[256],[0,256]
)

equalized_hist_g=cv2.calcHist(
    [equalized_rgb],[1],None,[256],[0,256]
)

equalized_hist_b=cv2.calcHist(
    [equalized_rgb],[2],None,[256],[0,256]
)

plt.subplot(2,2,4)

plt.plot(equalized_hist_r,label="Red")
plt.plot(equalized_hist_g,label="Green")
plt.plot(equalized_hist_b,label="Blue")

plt.title("Equalized Image Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.xlim([0,256])
plt.legend()

plt.tight_layout()
plt.show()
