#showing an image on opencv
import cv2 as cv
img=cv.imread(r'C:\tmp\0000.png')#The function destroyAllWindows destroys all of the opened HighGUI windows.
cv.imshow('image',img)#The function imshow displays an image in the specified window
cv.waitKey(0)#The function waitKey waits for a key event infinitely
cv.destroyAllWindows#The function destroyAllWindows destroys all of the opened HighGUI windows.
