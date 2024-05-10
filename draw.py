import cv2 as cv
import numpy as np
blank = np.zeros((500,500),dtype='uint8')
cv.imshow('Blank',blank)
img = cv.imread('photos\download.jpg')
cv.imshow('Cat',img)
cv.waitKey(70000)