#7.SOLID COLORS
#RED, GREEN , BLUE
import numpy as np
import cv2
img = np.zeros((500,500,3))
img[:] = 0,0,255 #BGR

cv2.imshow('RED',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
