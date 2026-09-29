import cv2 
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("color_back.jpg",cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error:image not found")
    exit()

r=img.astype(np.float32)

a=1.5
b=20

linear=a+r+b

linear=np.clip(linear,0,255)
linear=linear.astype(np.uint8)


c=255/np.log(1+np.max(r))
log_trans=c*np.log(1+r)

log_trans=np.clip(log_trans,0,255)
log_trans=log_trans.astype(np.uint8)

gamma = 0.5

normal=r/255.0
power=255*(normal*gamma)
power=power.astype(np.uint8)

plt.figure(figsize=(12,8))

plt.subplot(2, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(linear, cmap="gray")
plt.title("linear transformation")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(log_trans, cmap="gray")
plt.title("logarithmic tranformation")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(power, cmap="gray")
plt.title("power law transformation")
plt.axis("off")

plt.tight_layout()
plt.show()