from __future__ import unicode_literals
import youtube_dl
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip




from tqdm import tqdm
from glob import glob
import os

#v_uqiMw7tQ1Cc_0_56.mp4

files = sorted(glob("./ids_*.txt"))

OUTPUT_VIDEOS = './videos'
OUTPUT_VIDEOS_PROCESSED = "./videos_processed"
if os.path.exists(OUTPUT_VIDEOS) == False:
	os.makedirs(OUTPUT_VIDEOS)
if os.path.exists(OUTPUT_VIDEOS_PROCESSED) == False:
	os.makedirs(OUTPUT_VIDEOS_PROCESSED)


failcnt=0
succeedcnt = 0
for afile in files:
	arq = open(afile)
	type_file = afile.split("/")[-1].split("_")[1].split(".")[0]
	for line in tqdm(arq):
		print(line)
		_, name, start, end  = line.strip().split(".")[0].split("_")
		
		
		try:
			url='https://www.youtube.com/watch?v='+name
			download_path = OUTPUT_VIDEOS+"/"+ type_file
			if os.path.exists(download_path) == False:
				os.makedirs(download_path)
			

			ydl_opts = {
			    'outtmpl': os.path.join(download_path, name+".mp4"),
			    'ext': 'mp4',
			    'format': 'mp4'
			}

			with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			    ydl.download([url])



			
				
			succeedcnt += 1
			print('downloaded v_{}.mp4, total = {}'.format(name+".mp4", succeedcnt), flush=True)
		except Exception as e:
			print(e)
			failcnt += 1
			print('could not download {}.mp4, failcount = {}'.format(name+".mp4", failcnt), flush=True)
			continue

		
                



		dst_folder = os.path.join(OUTPUT_VIDEOS_PROCESSED, type_file)
		if os.path.exists(dst_folder) == False:
			os.makedirs(dst_folder)
		dst = os.path.join(dst_folder , "v_"+name+"_"+str(start)+"_"+str(end)+".mp4")
		
		ffmpeg_extract_subclip(os.path.join(download_path, name+".mp4"), int(start), int(end), targetname=dst)

print("Success", succeedcnt)
print("Failed", failcnt)
