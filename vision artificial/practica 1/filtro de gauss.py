import cv2
import matplotlib.pyplot as plt
import numpy as np

img= cv2.imread('C:\descarga chatgpt.png')
cv2.imshow('original',img)

f1=cv2.GaussianBlur(img,(3,3),0)

cv2.imshow('filtro de gauss',f1)
cv2.waitKey(0)
cv2.destroyAllWindows()