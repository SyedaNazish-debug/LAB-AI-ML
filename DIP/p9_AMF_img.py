# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# img = cv2.imreadimg = cv2.imread(
#     r"C:\Syeda_Nazish\practicle\DIP\ken-cheung.jpg",
#     cv2.IMREAD_GRAYSCALE
# )


# import cv2
# import os

# path = r"C:\Syeda_Nazish\practicle\DIP\ken-cheung.jpg"

# print("File exists:", os.path.exists(path))
# print("File path:", path)

# img = cv2.imread(path)

# print("Image loaded:", img is not None)

# if img is not None:
#     print("Image size:", img.shape)
# else:
#     print("OpenCV could not read the image.")


# if img is not None:
#     print("Image not found.")
# else:
#     kernel_size = 3
#     kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size ** 2)
#     kernel = kernel/(kernel_size * kernel_size)

#     filtered_img = cv2.filter2D(img, -1, kernel)

#     plt.figure(figsize=(10, 4))

#     plt.subplot(1, 2, 1)
#     plt.imshow(filtered_img, cmap='gray')
#     plt.title("ORIGINAL Image")
#     plt.axis("off")

#     plt.subplot(1, 2, 2)
#     plt.imshow(filtered_img, cmap='gray')
#     plt.title("FILTERED Image")
#     plt.axis("off")

#     plt.tight_layout()
#     plt.show()


import cv2
import numpy as np
import matplotlib.pyplot as plt

# Image path
path = r"C:\Syeda_Nazish\practicle\DIP\ken-cheung.jpg"

# Read image in grayscale
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

# Check image
if img is None:
    print("Error: Image could not be loaded.")
    exit()

print("Image loaded successfully!")
print("Image size:", img.shape)

# 3 x 3 Arithmetic Mean Filter
kernel_size = 3

kernel = np.ones(
    (kernel_size, kernel_size),
    np.float32
)

kernel = kernel / (kernel_size * kernel_size)

# Apply mean filter
filtered_img = cv2.filter2D(img, -1, kernel)

# Display
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("Original Grayscale Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(filtered_img, cmap="gray")
plt.title("Arithmetic Mean Filter")
plt.axis("off")

plt.tight_layout()
plt.show()