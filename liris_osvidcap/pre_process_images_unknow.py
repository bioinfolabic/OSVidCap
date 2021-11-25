import pickle
import os
import cv2 as cv
from tqdm import tqdm 

BLUR  = True

 
def blur_frame(img_path, img_dst, x, y, x2, y2):	
	global BLUR
	img = cv.imread(img_path)
	blur = img
	if BLUR == True:
		blur = cv.blur(img,(35,35))
		blur[y:y2, x:x2] = img[y:y2, x:x2]
	cv.imwrite(img_dst, blur)




data = pickle.load(open("spatial_temporal_unknown_actions.pickle", "rb"))
for folder in data.keys():
	print(folder)
	output_dir = folder+"_processed_unknown/"
	for  video in tqdm(data[folder].keys()):
		for segment in data[folder][video].keys():
			frames_list = data[folder][video][segment]
			for aFrame in frames_list.keys():
				bbox = frames_list[aFrame]
				src = os.path.join(folder, video, "rgb-"+str(aFrame)+".jpg")
				dst_folder = os.path.join(output_dir, video, segment)
				if os.path.exists(dst_folder) == False:
					os.makedirs(dst_folder)
				dst = os.path.join(dst_folder, "rgb-"+str(aFrame)+".jpg")
				blur_frame(src, dst, bbox[0], bbox[1], bbox[2], bbox[3])
