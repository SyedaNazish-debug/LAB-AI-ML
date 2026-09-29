import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("color_back.jpg")

if img is None:
    print("Error : image not found")
    exit()

rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

R=rgb[:,:,0]

G=rgb[:,:,1]

B=rgb[:,:,2]

r=R.astype(float)/255.0
g=G.astype(float)/255.0
b=B.astype(float)/255.0

I=(r+g+b)/3.0

minimum = np.minimum(np.minimum(r,g),b)

S=1-(3*minimum/(r+g+b+ 1e-10))

num=0.5 * ((r-g)+(r-b))
den=np.sqrt((r-g)**2+(r-b)*(g-b))

cos_theta=num/(den + 1e-10)
cos_theta=np.clip(cos_theta,-1,1)
theta=np.arccos(cos_theta)

H=np.where (b<=g,theta , 2 * np.pi - theta)
H=H*180/np.pi

Y=0.299 * r + 0.587 * g + 0.114 * b
YI=0.596 * r - 0.274 * g - 0.322 * b
YQ= 0.211 * r - 0.523 * g + 0.312 * b

plt.figure(figsize=(12,10))

plt.subplot(3,4,1)
plt.imshow(rgb)
plt.title("Original RGB")
plt.axis("off")

plt.subplot(3, 4, 2)
plt.imshow(R, cmap="gray") 
plt.title("Red") 
plt.axis("off") 

plt.subplot(3, 4, 3)
plt.imshow(G, cmap="gray") 
plt.title("Green") 
plt.axis("off") 

plt.subplot(3, 4, 4)
plt.imshow(B, cmap="gray") 
plt.title("Blue") 
plt.axis("off")  

plt.subplot(3, 4, 5)
plt.imshow(H, cmap="hsv") 
plt.title("Hue") 
plt.axis("off")

plt.subplot(3, 4, 6)
plt.imshow(S, cmap="gray")
plt.title("Saturation") 
plt.axis("off")  

plt.subplot(3, 4, 7) 
plt.imshow(I, cmap="gray") 
plt.title("Intensity")
plt.axis("off")  

plt.subplot(3, 4, 8)
plt.imshow(Y, cmap="gray") 
plt.title("Y - Luminance") 
plt.axis("off")

plt.subplot(3, 4, 9)
plt.imshow(YI, cmap="gray")
plt.title("I - Chrominance")
plt.axis("off")

plt.subplot(3, 4, 10)
plt.imshow(YQ, cmap="gray") 
plt.title("Q - Chrominance")
plt.axis("off") 

plt.tight_layout() 
plt.show()

plt.tight_layout() 
plt.show() 