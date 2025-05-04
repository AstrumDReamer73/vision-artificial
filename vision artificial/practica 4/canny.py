import cv2
import matplotlib.pyplot as plt

img = cv2.imread('C:\\descarga chatgpt.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

bordes = cv2.Canny(img_gray, 100, 200)

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.title('Original (Gris)')
plt.imshow(img_gray, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Canny (bordes)')
plt.imshow(bordes, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
