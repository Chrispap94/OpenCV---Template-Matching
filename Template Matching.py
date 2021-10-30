import cv2
import numpy as np

#load image and test
img=cv2.imread('img3.jpeg',cv2.IMREAD_UNCHANGED)
test=cv2.imread('test3.jpeg',cv2.IMREAD_UNCHANGED)

cv2.imshow('image',img)
cv2.waitKey()

cv2.imshow('itest',test)
cv2.waitKey()

res=cv2.matchTemplate(img,test,cv2.TM_CCOEFF_NORMED)

cv2.imshow('heat map',res)
cv2.waitKey()

value_min,value_max,location_min,location_max=cv2.minMaxLoc(res)

width=test.shape[1]
height=test.shape[0]

#sensitivity threshold
threshold= .90
yloc,xloc=np.where(res>=threshold)

#reduce rectangles
rect=[]
for (x,y) in zip(xloc,yloc):
    rect.append([int(x),int(y),int(width),int(height)])
    rect.append([int(x),int(y), int(width),int(height)])

rect,weights=cv2.groupRectangles(rect,1,0.2)


for (x,y,w,h) in rect:
    img = cv2.rectangle(img,(x,y),(x+width,y+height),(0,255,255),2)


#detection
cv2.imshow('detection', img)
cv2.waitKey()
