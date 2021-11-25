import cv2 as cv
import numpy as np
import os
from glob import glob
import xml.etree.ElementTree as ET 
from tqdm import tqdm

def blur_frame(img_path, img_dst, x, y, w, h):	
	img = cv.imread(img_path)
	blur = cv.blur(img,(35,35))
	blur[y:y+h, x:x+w] = img[y:y+h, x:x+w]
	cv.imwrite(img_dst, blur)
	return blur



folders = ['training-validation', 'test']
for folder in folders: 	
	output_dir = folder+"_processed"

	if not os.path.isdir(output_dir): 
		os.mkdir(output_dir)

	files_xml = sorted(glob(os.path.join(folder, '*.xml')))
	print("Processing", folder)
	for axml in tqdm(files_xml):

		name_video = axml.split("/")[-1].split(".")[0]

		output_dir_video = os.path.join(output_dir, name_video)
		if not os.path.isdir(output_dir_video):
			os.mkdir(output_dir_video)

		arq = open(axml, 'rb')
		tree = ET.parse(arq) 
		root = tree.getroot() 
		for item in root.findall('./video'):
			
			for action in item:
				newItem = {}
				if action.tag == 'videoName': continue
	
				fr_ini = 99999
				fr_fim = -99999
				tmp_dict = {}
				for child in action:
					if int(child.attrib['framenr']) < fr_ini:
						fr_ini = int(child.attrib['framenr'])
					if int(child.attrib['framenr']) > fr_fim:
						fr_fim = int(child.attrib['framenr'])
					tmp_dict[child.attrib['framenr']] = {'x': child.attrib['x'], 'y': child.attrib['y'], 'width': child.attrib['width'], 'height':  child.attrib['height'] } 
				
				output_frames = os.path.join(output_dir_video, action.attrib['class']+"_"+str(fr_ini)+"_"+str(fr_fim))
				if not os.path.isdir(output_frames):
					os.mkdir(output_frames)
				for num_frame in tmp_dict.keys():

					frame_src = os.path.join(folder, name_video, 'rgb-{:06d}.jpg'.format(int(num_frame)))
					frame_dst = os.path.join(output_frames, 'rgb-{:06d}.jpg'.format(int(num_frame)))
					
					if not os.path.exists(frame_src): 
						continue
					delta = 25
					blur_frame(frame_src, frame_dst, int(tmp_dict[num_frame]['x'])-delta, int(tmp_dict[num_frame]['y'])-delta, int(tmp_dict[num_frame]['width'])+delta, int(tmp_dict[num_frame]['height'])+delta)

