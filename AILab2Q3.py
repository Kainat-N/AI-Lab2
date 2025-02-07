import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio  # To read image files


img_path = "test.jpg"
img_array = imageio.imread(img_path)


plt.figure(figsize=(10, 5))

plt.subplot(1, 4, 1)
plt.imshow(img_array)
plt.title("Original Image")
plt.axis("off")


rotated_img = np.rot90(img_array)
plt.subplot(1, 4, 2)
plt.imshow(rotated_img)
plt.title("Rotated Image")
plt.axis("off")


flipped_img = np.fliplr(img_array)
plt.subplot(1, 4, 3)
plt.imshow(flipped_img)
plt.title("Flipped Image")
plt.axis("off")

gray_img = np.dot(img_array[..., :3], [0.299, 0.587, 0.114])
plt.subplot(1, 4, 4)
plt.imshow(gray_img, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")

# Show all images
plt.tight_layout()
plt.show()
