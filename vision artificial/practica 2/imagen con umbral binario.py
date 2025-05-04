import cv2
import matplotlib.pyplot as plt

img = cv2.imread('C:\descarga chatgpt.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar umbral binario: píxeles > 127 se vuelven 255, el resto se vuelve 0
_, img_binaria = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)


plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.title('Grises')
plt.imshow(img_gray, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Umbral binario')
plt.imshow(img_binaria, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
