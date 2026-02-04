import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("example.jpg")
image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

(h,w) = image.shape[:2]
center = (w//2, h//2)

M = cv2.getRotationMatrix2D(center,45,1.0)
rotated = cv2.warpAffine(image_rgb,M,(w,h))
plt.imshow(rotated)
plt.title("Rotated Image")
plt.show()

image.shape

brightness_matrix = np.ones(image.shape,dtype = "uint8") * 50
brighter = cv2.add(image, brightness_matrix)

brighter_rgb = cv2.cvtColor(brighter,cv2.COLOR_BGR2RGB)
plt.imshow(brighter_rgb)
plt.title("Brighter Image")
plt.show()
