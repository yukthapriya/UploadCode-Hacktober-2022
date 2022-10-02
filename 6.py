#6.SOLID BACKGROUND
#CREATE WHITE OR BLACK BACKGROUND
import numpy as np
import cv2

img = np.ones((500,500,3))
cv2.imshow('White background',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
