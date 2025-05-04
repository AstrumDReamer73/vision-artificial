import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('C:\\descarga chatgpt.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sobelx = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=3)
sobelx_abs = cv2.convertScaleAbs(sobelx)

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.title('Original (Gris)')
plt.imshow(img_gray, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Sobel X (bordes verticales)')
plt.imshow(sobelx_abs, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
