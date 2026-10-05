import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Get the folder where this Python file is located
folder = os.path.dirname(os.path.abspath(__file__))

# Image path
image_path = os.path.join(folder, "color_back.jpg")

# Check whether image exists
print("Image path:", image_path)
print("File exists:", os.path.exists(image_path))

# Read grayscale image
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Check whether image was loaded
if img is None:
    print("Error: Image could not be loaded. Check file path/integrity.")
    exit()

print("Image loaded successfully.")

# Gaussian noise parameters
mean = 0
sigma = 25

# Generate Gaussian noise
noise = np.random.normal(mean, sigma, img.shape)

# Add noise
noisy_img = img + noise

# Keep pixel values between 0 and 255
noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)

# Display
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(noisy_img, cmap="gray")
plt.title("Gaussian Noisy Image")
plt.axis("off")

plt.show()