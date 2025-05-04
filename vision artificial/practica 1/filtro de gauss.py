import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread('C:\descarga chatgpt.png')
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

f1=cv2.GaussianBlur(img,(15,15),0)
f1=cv2.cvtColor(f1,cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.title('Original')
plt.imshow(img_rgb)
plt.axis('Off')

plt.subplot(1,2,2)
plt.title('filtro de gauss')
plt.imshow(f1)
plt.axis('Off')

plt.tight_layout()
plt.show()
