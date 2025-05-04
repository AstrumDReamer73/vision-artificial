import cv2
import matplotlib.pyplot as plt

img= cv2.imread('C:\descarga chatgpt.png')
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

f1=cv2.blur(img,(15,15))
f1=cv2.cvtColor(f1,cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.title('Original')
plt.imshow(img_rgb)
plt.axis('Off')

plt.subplot(1,2,2)
plt.title('filtro promedio')
plt.imshow(f1)
plt.axis('Off')

plt.tight_layout()
plt.show()