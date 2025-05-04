import cv2
import matplotlib.pyplot as plt

img= cv2.imread('C:\descarga chatgpt.png')
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) 

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.title('Original')
plt.imshow(img_rgb)
plt.axis('Off')

plt.subplot(1,2,2)
plt.title('escala de grises')
plt.imshow(img_gray,cmap='gray')
plt.axis('Off')

plt.tight_layout()
plt.show()