import cv2
import dlib
import numpy

fname = "face.jpg"
im = cv2.imread(fname, cv2.IMREAD_COLOR)
print(im.shape[:2])