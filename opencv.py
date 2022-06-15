import cv2
kath = 'building.jpg'
hello = 'Have a great day!'
ImageProcess = cv2.imread(kath, 1)
cv2.imshow(hello, ImageProcess)
cv2.waitKey(0)
cv2.destroyAllWindows()