import cv2
import os
import sys


print(sys.argv[1])

img_name = 'output_dir/images/'+sys.argv[1]+'_none.jpg'
fname = 'output_dir/labels/'+sys.argv[1]+'_none.txt'

lines = open(fname).read()
lines = lines.split('\n')
img = cv2.imread(img_name)
H, W, C = img.shape

for l in lines[:-1]:
	x,y,w,h = l.split(' ')[1:]
	w,h = int(float(w)*W),int(float(h)*H)
	x1,y1,x2,y2 = int(float(x)*W-w/2),int(float(y)*H-h/2),int(float(x)*W+w/2),int(float(y)*H+h/2)
	print(x1,y1,x2,y2)
	cv2.rectangle(img,(x1,y1),(x2,y2),(0,225,225),2)


cv2.imshow("image_plot",img)
cv2.waitKey(0)
cv2.imwrite("imag.jpg",img)

