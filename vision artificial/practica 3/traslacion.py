import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('C:\\descarga chatgpt.png')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

matriz_traslacion = np.float32([[1, 0, 100], [0, 1, 50]])

alto, ancho = img.shape[:2]
img_trasladada = cv2.warpAffine(img, matriz_traslacion, (ancho, alto))
img_trasladada_rgb = cv2.cvtColor(img_trasladada, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.title('Original')
plt.imshow(img_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Trasladada')
plt.imshow(img_trasladada_rgb)
plt.axis('off')

plt.tight_layout()
plt.show()
