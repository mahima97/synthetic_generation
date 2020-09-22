from __future__ import division
import numpy as np
import os
import cv2
from tqdm import tqdm

imgpath = 'output_dir/images'
labelpath = 'output_dir/labels'
debugpath = 'output_dir/boxes'

imgs = os.listdir(imgpath)
labels = os.listdir(labelpath)


count_small = 0
count_medium = 0
count_large = 0 
count_files = 0



res = 416
area_small = 32 * 32 / (res ** 2)
area_medium = 96 * 96 / (res ** 2)

def get_area(boxes):
	area = [(box[3] * box[4]) for box in boxes]
	return np.array(area)

def convert_from_YOLO(bbox, width, height):
	# print(bbox)
	# _ , xc, yc, w, h = np.split(bbox, 5, axis=1)
	xc, yc, w, h = bbox[1:]

	xmin = (xc * width)  - (w * width) / 2.    
	xmax = xmin + (w * width)

	ymin = (yc * height)  - (h * height) / 2.    
	ymax = ymin + (h * height)

	return np.hstack((xmin, ymin, xmax, ymax))

def draw_bbox(image, bboxes, color=(255, 0, 0)):
	H, W, C = image.shape
	
	for bbox in bboxes:
		bb = convert_from_YOLO(bbox,W,H)
		bb = bb.astype(int)
		cv2.rectangle(image, (bb[0], bb[1]), (bb[2], bb[3]), color ,1)


for label in tqdm(labels):
	
	data = np.loadtxt(os.path.join(labelpath, label))

	if data.shape[0] > 0:


		img  = cv2.imread(os.path.join(imgpath, label[:-3]+'jpg'))
		data = data if data.ndim > 1 else data.reshape(1, -1)

		area = get_area(data)

		draw_bbox(img,data)
		cv2.imwrite(debugpath+'/'+label[:-3]+'jpg',img)
		

		count_small += (np.sum(area < area_small))
		count_medium += (np.sum((area >= area_small) & (area < area_medium)))
		count_large += (np.sum(area >= area_medium))

		count_files += 1

print("Small: %d ||| Medium: %d ||| Large: %d ||| Files %d" %(count_small, count_medium, count_large, count_files))









