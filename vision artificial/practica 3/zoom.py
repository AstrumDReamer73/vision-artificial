import cv2
import matplotlib.pyplot as plt

img = cv2.imread('C:\\descarga chatgpt.png')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

zoom = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
zoom_rgb = cv2.cvtColor(zoom, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title('Original')
plt.imshow(img_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Zoom x2')
plt.imshow(zoom_rgb)
plt.axis('off')

plt.tight_layout()
plt.show()
