import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('C:\\descarga chatgpt.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sobel_y = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, ksize=3)
sobel_y_magnitude = np.uint8(np.absolute(sobel_y))

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title('Original (Gris)')
plt.imshow(img_gray, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Sobel Y (bordes verticales)')
plt.imshow(sobel_y_magnitude, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
