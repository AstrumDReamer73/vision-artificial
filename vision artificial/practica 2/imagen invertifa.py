import cv2
import matplotlib.pyplot as plt

img = cv2.imread('C:\\descarga chatgpt.png')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img_invertida = cv2.bitwise_not(img)
img_invertida_rgb = cv2.cvtColor(img_invertida, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.title('Original')
plt.imshow(img_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Invertida (Negativo)')
plt.imshow(img_invertida_rgb)
plt.axis('off')

plt.tight_layout()
plt.show()
