
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from pathlib import Path

image_path = Path(__file__).parent / "color_back.jpg"

image = Image.open(image_path).convert("L")
image = Image.open("NN_PRACTICLE/color_back.jpg").convert("L")

# Convert image to NumPy array
img = np.array(image, dtype=float)


# Convolution function
def convolution(image, kernel):
    kernel_size = kernel.shape[0]
    pad = kernel_size // 2

    # Add padding around the image
    padded_image = np.pad(
        image,
        ((pad, pad), (pad, pad)),
        mode="edge"
    )

    # Create output image
    output = np.zeros_like(image)

    # Perform convolution
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):

            region = padded_image[
                i:i + kernel_size,
                j:j + kernel_size
            ]

            output[i, j] = np.sum(region * kernel)

    # Keep pixel values between 0 and 255
    output = np.clip(output, 0, 255)

    return output


# -----------------------------
# Define convolution kernels
# -----------------------------

# Blur kernel
blur_kernel = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]) / 9


# Sharpen kernel
sharpen_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])


# Edge detection kernel
edge_kernel = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])


# -----------------------------
# Apply convolution
# -----------------------------

blur_image = convolution(img, blur_kernel)

sharpen_image = convolution(img, sharpen_kernel)

edge_image = convolution(img, edge_kernel)


# -----------------------------
# Display results
# -----------------------------

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("Original Grayscale Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(blur_image, cmap="gray")
plt.title("Blurred Image")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(sharpen_image, cmap="gray")
plt.title("Sharpened Image")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(edge_image, cmap="gray")
plt.title("Edge Detection")
plt.axis("off")

plt.tight_layout()
plt.show()
