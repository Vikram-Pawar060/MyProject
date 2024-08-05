import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
image_path = 'D:\mini project\image smoothing\img.jpg'
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Gaussian Blur
gaussian_blur = cv2.GaussianBlur(image, (15, 15), 0)

# Median Filter
median_blur = cv2.medianBlur(image, 15)

# Bilateral Filter
bilateral_blur = cv2.bilateralFilter(image, 15, 75, 75)

# Save the resulting images
cv2.imwrite('gaussian_blur.jpg', cv2.cvtColor(gaussian_blur, cv2.COLOR_RGB2BGR))
cv2.imwrite('median_blur.jpg', cv2.cvtColor(median_blur, cv2.COLOR_RGB2BGR))
cv2.imwrite('bilateral_blur.jpg', cv2.cvtColor(bilateral_blur, cv2.COLOR_RGB2BGR))

# Display the results
titles = ['Original Image', 'Gaussian Blur', 'Median Blur', 'Bilateral Blur']
images = [image, gaussian_blur, median_blur, bilateral_blur]

plt.figure(figsize=(12, 6))
for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
