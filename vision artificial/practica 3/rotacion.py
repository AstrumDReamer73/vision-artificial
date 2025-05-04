import cv2
import matplotlib.pyplot as plt

img = cv2.imread('C:\descarga chatgpt.png')
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

alto,ancho=img.shape[:2]
centro=(ancho//2,alto//2)
matriz_rotada=cv2.getRotationMatrix2D(centro,45,1.0)

img_rotada = cv2.warpAffine(img, matriz_rotada, (ancho, alto))
img_rotada_rgb = cv2.cvtColor(img_rotada, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.title('Original')
plt.imshow(img_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Rotada 45°')
plt.imshow(img_rotada_rgb)
plt.axis('off')

plt.tight_layout()
plt.show()