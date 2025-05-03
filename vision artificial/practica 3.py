import cv2
import matplotlib.pyplot as plt

img= cv2.imread('C:\descarga chatgpt.png')

#convertir la imagen a HSV
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

plt.imshow(img_hsv)
plt.title("imagen en HSV")
plt.axis('off')
plt.show()

#convertir la imagen a YUV
img_yuv=cv2.cvtColor(img,cv2.COLOR_BGR2YUV)

plt.imshow(img_yuv)
plt.title("imagen en yuv")
plt.axis('off')
plt.show()