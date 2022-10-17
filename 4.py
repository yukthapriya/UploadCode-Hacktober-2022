#Arthmetic operations on opencv
#we can add two images using cv2.add() function and subtract using subtract() function
import cv2 as cv
img1=cv.imread(r'C:\tmp\sample1.png')
img2=cv.imread(r'C:\tmp\sample2.png')
add=cv.add(img1,img2)
cv.imshow('added',add)
if cv.waitKey(0) & 0xff==27:
    cv.destroyAllWindows()
