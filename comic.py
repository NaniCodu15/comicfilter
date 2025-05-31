import cv2
import numpy as np

# Cargar imagen
imagen = cv2.imread('image.png')
if imagen is None:
    print("No se pudo cargar")
    exit()

#Suavizar
imagen_suave = cv2.bilateralFilter(imagen, d=9, sigmaColor=200, sigmaSpace=200)

#escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

bordes = cv2.Canny(imagen_gris, 50, 150)

#Invertir bordes
bordes_inv = cv2.bitwise_not(bordes)

#conversión de bordes
bordes_color = cv2.cvtColor(bordes_inv, cv2.COLOR_GRAY2BGR)

imagen_comic = cv2.bitwise_and(imagen_suave, bordes_color)


cv2.imshow('Original', imagen)
cv2.imshow('Comic', imagen_comic)
cv2.resizeWindow('Original', 700, 900)
cv2.resizeWindow('Comic', 800, 900)

cv2.waitKey(0)
cv2.destroyAllWindows()


