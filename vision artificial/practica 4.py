import cv2
import matplotlib.pyplot as plt
import numpy as np

img= cv2.imread('C:\descarga chatgpt.png')

print("dimensiones de la imagen: ",img.shape)

print("Valores de los primeros 5 pixeles en la primera fila: ")
print(img[0,:5])
