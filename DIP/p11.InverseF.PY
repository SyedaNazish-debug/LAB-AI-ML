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

img = cv2.resize(img, (512, 512))

kernel = 15
sigma = 5

kernel_id=cv2.getGaussianKernel(kernel, sigma)
psf=kernel_id @ kernel_id.T
psf = psf / np.sum(psf)

rows,cols= img.shape[:2]
psf_padded = np.zeros((rows, cols), dtype=np.float32)

center_y =rows//2
center_x = cols//2

half = kernel//2

psf_padded[center_y-half:center_y+half+1,
        center_x-half:center_x+half+1
    ] = psf

psf_padded = np.fft.ifftshift(psf_padded)

h=np.fft.fft2(psf_padded)

degraded_img = np.zeros_like(img, dtype=np.float32)

for c in range(3):

    channel = img[:, :, c].astype(np.float32)

    F = np.fft.fft2(channel)

    G = F * h

    degraded_img[:, :, c] = np.real(
        np.fft.ifft2(G)
    )
degraded = np.clip(degraded_img, 0, 255).astype(np.uint8)
restored_img= np.zeros_like(degraded_img,dtype=np.float32)
epsilon=1e-3

for c in range(3):
    G =np.fft.fft2(
        degraded_img[:, :, c]
    )
    F_estimated = G/(h + epsilon)
    restored_img[:, :, c] = np.real(
        np.fft.ifft2(F_estimated)
        )
restored_img = np.clip(
    restored_img, 0, 255).astype(np.uint8)

original = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
degraded = cv2.cvtColor(degraded, cv2.COLOR_BGR2RGB)
restored = cv2.cvtColor(restored_img, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
plt.imshow(original)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(degraded)
plt.title('Degraded Image')
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(restored)
plt.title('Restored Image')
plt.axis('off')


plt.tight_layout()
plt.show()
