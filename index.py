import numpy as np
import cv2

image = np.zeros((300, 600, 3),np.uint8)

image[1:150, :, 2] = 255
image[150:300,:,0:] = 255

print("INDONESIA MERDEKA!!!")
cv2.imshow(image);
