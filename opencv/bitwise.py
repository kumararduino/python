import cv2
import numpy as np
rect = np.zeros((300,300),dtype= 'uint8')
circle = np.zeros((300,300),dtype = 'uint8')
rect = cv2.rectangle(rect,(25,25),(275,275),255,-1)
circle = cv2.circle(circle,(150,150),150,255,-1)
bitand = cv2.bitwise_and(rect,circle)
cv2.imshow('and',bitand)
bitor = cv2.bitwise_or(rect,circle)
cv2.imshow('or',bitor)
bitnot = cv2.bitwise_not(circle)
cv2.imshow('not',bitnot)
bitxor = cv2.bitwise_xor(rect,circle)
cv2.imshow('xor',bitxor)
cv2.waitKey(0)
cv2.destroyAllWindows()
