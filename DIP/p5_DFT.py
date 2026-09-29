import cv2
import numpy as np
import matplotlib.pyplot as plt


img=cv2.imread("color_back.jpg")

if img is None:
    print("error : image not found")
    exit()
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray=np.float32(gray)

dft=cv2.dft(gray,flags=cv2.DFT_COMPLEX_OUTPUT)

dft_shift=np.fft.fftshift(dft)

magnitude=cv2.magnitude(
    dft_shift[:,:,0],
    dft_shift[:,:,1]
)

magnitude_spc=20*np.log(magnitude+1)

original=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
plt.imshow(original)
plt.title("Original Image")
plt.axis("off")

plt.subplot(2,2,2)
plt.imshow(gray,cmap="gray")
plt.title("Grayscale image")
plt.axis("off")

plt.subplot(2,2,3)
plt.imshow(magnitude_spc,cmap="gray")
plt.title("DFT magnitude spectrum")
plt.axis("off")

plt.subplot(2,2,4)
plt.imshow(magnitude_spc,cmap="jet")
plt.title("Frequency components")
plt.axis("off")

plt.tight_layout()
plt.show()