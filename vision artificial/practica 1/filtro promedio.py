import cv2
import matplotlib.pyplot as plt
import numpy as np

img= cv2.imread('C:\descarga chatgpt.png')
cv2.imshow('original',img)

f2=cv2.blur(img,-1,{3,3})

cv2.imshow('filtro de media',f1)
cv2.waitKey(0)
cv2.destroyAllWindows()

