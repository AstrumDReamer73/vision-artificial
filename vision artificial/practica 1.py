import cv2
import matplotlib.pyplot as plt

img= cv2.imread('C:\descarga chatgpt.png')

img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.imshow(img_rgb)
plt.title("imagen normal")
plt.axis('off')
plt.show()