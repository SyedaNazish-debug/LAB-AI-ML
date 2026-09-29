import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import colorsys

img=Image.open("images.jpeg").convert("RGB")
rgb=np.array(img, dtype=np.float32)/255.0

R=rgb[:,:,0]
G=rgb[:,:,1]
B=rgb[:,:,2]

I=(R+G+B)/3.0

total=R=G+B
minimum=np.minimum(np.minimum(R,G),B)

S=np.zeros_like(I)
mask = total>0

S[mask]=1-(3*minimum[mask]/total[mask])

num=0.5*(R-G)+(R-B)
den=np.sqrt((R-G)**2+(R-B)*(R-G))

theta=np.arccos(
    np.clip(num/(den + 1e-10),-1,1)
)

H= np.where(B>G, 2*np.pi - theta , theta)
H[den < 1e-10]=0
H=H/(2*np.pi)

Y = 0.299 * R + 0.587 * G + 0.114 * B
IQ_I = 0.596 * R - 0.274 * G - 0.322 * B 
Q = 0.211 * R - 0.523 * G + 0.312 * B

fig, ax = plt.subplots(3, 4, figsize=(14, 10))

ax[0, 0].imshow(rgb)
ax[0, 0].set_title("Original RGB Image") 
ax[0, 1].imshow(R, cmap="gray", vmin=0, vmax=1) 
ax[0, 1].set_title("Red Component") 
ax[0, 2].imshow(G, cmap="gray", vmin=0, vmax=1) 
ax[0, 2].set_title("Green Component")
ax[0, 3].imshow(B, cmap="gray", vmin=0, vmax=1)
ax[0, 3].set_title("Blue Component")

ax[1, 0].imshow(H, cmap="hsv", vmin=0, vmax=1)
ax[1, 0].set_title("Hue (H)")
ax[1, 1].imshow(S, cmap="gray", vmin=0, vmax=1)
ax[1, 1].set_title("Saturation (S)")
ax[1, 2].imshow(I, cmap="gray", vmin=0, vmax=1)
ax[1, 2].set_title("Intensity (I)")
ax[1, 3].axis("off")

ax[2, 0].imshow(Y, cmap="gray", vmin=0, vmax=1) 
ax[2, 0].set_title("Luminance (Y)")

ax[2, 1].imshow(IQ_I, cmap="gray",vmin=-0.6, vmax=0.6)
ax[2, 1].set_title("In-phase (I)")
ax[2, 2].imshow(Q, cmap="gray",vmin=-0.6, vmax=0.6) 
ax[2, 2].set_title("Quadrature (Q)")
ax[2, 3].axis("off") 

for a in ax.flat:    
    a.axis("off") 
    plt.tight_layout()
    plt.show()