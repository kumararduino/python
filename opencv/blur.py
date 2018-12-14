import cv2
img = cv2.imread('snake.png',1)
blur = cv2.GaussianBlur(img,(5,5),1)
blurr = cv2.blur(img,(5,5))
b = cv2.medianBlur(img,5)
bb = cv2.bilateralFilter(img,9,75,75)
cv2.imshow('gaussian',blur)
cv2.imshow('blur',blurr)
cv2.imshow('median',b)
cv2.imshow('original',img)
cv2.imshow('bilateral',bb)
cv2.waitKey(0)
cv2.destroyAllWindows()
