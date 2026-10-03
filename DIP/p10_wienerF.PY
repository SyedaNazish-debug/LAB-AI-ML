import cv2
import numpy as np 
import matplotlib.pyplot as plt

path =r"c:\Syeda_Nazish\practicle\DIP\noisy_img.jpg"

img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Image could not be loaded.")
    exit()

print("Image loaded successfully.")
print("Image shape:", img.shape)

img_float = img.astype(np.float32)

mean = 0
sigma = 35

noise = np.random.normal(
    mean,
    sigma,
    img_float.shape
).astype(np.float32)

noise_img = img_float + noise

noisy_img = np.clip(noise_img,0,255)

noise_var = sigma ** 2

kernel_size = 7

local_mean = cv2.boxFilter(
    noisy_img,
    -1,
    (kernel_size, kernel_size)
)

local_mean_square = cv2.boxFilter(
    noisy_img ** 2,
    -1,
    (kernel_size, kernel_size)
)

local_var =local_mean_square - local_mean**2

epliosn = 1e-8

wiener_img = local_mean + (np.maximum(local_var - noise_var, 0)
    / (local_var + epliosn)
    ) * (noisy_img - local_mean)

wiener_img = np.clip(wiener_img, 0, 255)
noisy_img = noisy_img.astype(np.uint8)
wiener_img = wiener_img.astype(np.uint8)

plt.figure(figsize=(12,6))

plt.subplot(1,3,1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt

plt.subplot(1,3,2)
plt.imshow(noisy_img, cmap='gray')
plt.title('Noisy Image')
plt

plt.subplot(1,3,3)
plt.imshow(wiener_img, cmap='gray')
plt.title('Wiener Filtered Image')

plt.tight_layout()
plt.show()