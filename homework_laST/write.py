import glob
import cv2 as cv

path = glob.glob("homework_laST/w.img")
cv_img = []
for img in path:
    n = cv.imread(img)
    cv_img.append(n)

