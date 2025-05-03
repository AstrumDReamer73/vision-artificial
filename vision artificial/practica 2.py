import cv2
import matplotlib.pyplot as plt

img= cv2.imread('C:\descarga chatgpt.png')
    
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

plt.imshow(img_gray,cmap='gray')
plt.title("imagen en escala de grises")
plt.axis('off')
plt.show()