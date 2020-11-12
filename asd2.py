import speech_recognition as sr 
from moviepy.editor import *
import cv2 
import arabic_reshaper
from bidi.algorithm import get_display
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import time
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from googletrans import Translator, constants
from pprint import pprint

translator = Translator()
clip = VideoFileClip(r"a2.mp4")
value = clip.end 
value=int(value)/5
print("End Time : ", end =" ") 
print(value) 
n=0
start_time=0
end_time=5
'''while n<=int(value):
	try:
		ffmpeg_extract_subclip("a2.mp4", start_time , end_time, targetname="vid/test"+str(n)+".mp4")
		n+=1
		start_time+=5
		end_time+=5
	except Exception as e:
		print(e)
		break'''
n=0
while  n<=int(value):
 try:
 	clip = VideoFileClip(r"a2.mp4")
 	clip.audio.write_audiofile(r'wav/converted.wav')
 	n+=1
 except Exception as e:
 	break

n=0
qw=0
qw2=5
mw=0
hw=0
while  n<int(value):
	translator = Translator()
	r = sr.Recognizer()
	audio = sr.AudioFile('wav/converted.wav')
	with audio as source:
	  audio_file = r.record(source)
	try:
		result=r.recognize_google(audio_file)
	except Exception as e:
		result=" "
		print("None")
	# translate a spanish text to arabic for instance
	try:
		translation = translator.translate(result, dest="ar")
	except Exception as e:
		translation=" "
		print("None")

	with open('a2.srt',mode ='a', encoding="utf-8") as file:
	   file.write("\n")
	   file.write(str(n+1))
	   file.write("\n")
	   if qw2 <10 and mw<10:
	   	file.write("0"+str(hw)+":0"+str(mw)+":0"+str(qw)+",000 -->  0"+str(hw)+":0"+str(mw)+":0"+str(qw2)+",000")
	   elif qw2 >= 10 and mw<10:
	   	file.write("0"+str(hw)+":0"+str(mw)+":0"+str(qw)+",000 -->  0"+str(hw)+":0"+str(mw)+":"+str(qw2)+",000")
	   elif qw <10 and mw<10:
	   	file.write("0"+str(hw)+":0"+str(mw)+":0"+str(qw)+",000 -->  0"+str(hw)+":0"+str(mw)+":"+str(qw2)+",000")
	   elif qw >= 10 and mw<10:
	   	file.write("0"+str(hw)+":0"+str(mw)+":"+str(qw)+",000 -->  0"+str(hw)+":0"+str(mw)+":"+str(qw2)+",000")
	   elif qw2 <10 and mw>=10:
	   	file.write("0"+str(hw)+":"+str(mw)+":0"+str(qw)+",000 -->  0"+str(hw)+":0"+str(mw)+":0"+str(qw2)+",000")
	   elif qw2 >= 10 and mw>=10:
	   	file.write("0"+str(hw)+":"+str(mw)+":0"+str(qw)+",000 -->  0"+str(hw)+":0"+str(mw)+":"+str(qw2)+",000")
	   elif qw <10 and mw>=10:
	   	file.write("0"+str(hw)+":"+str(mw)+":0"+str(qw)+",000 -->  0"+str(hw)+":0"+str(mw)+":"+str(qw2)+",000")
	   elif qw >= 10 and mw>=10:
	   	file.write("0"+str(hw)+":"+str(mw)+":"+str(qw)+",000 -->  0"+str(hw)+":0"+str(mw)+":"+str(qw2)+",000")
	   file.write("\n")
	   file.write(translation.text) 
	   file.write("\n")
	   print(translation.text)
	   print("Doen "+str(n))
	n+=1
	qw+=5
	qw2+=5
	if qw==60:
		qw=0
		qw2=5
		mw+=1
	elif mw==60:
		hw+=1

#while True:'''

#movepy save 
'''clip = VideoFileClip(r"test"+str(e1)+".mp4")
# clipping of the video   
# getting video for only starting 10 seconds  
clip = clip.subclip(0, 10)  
    
# Reduce the audio volume (volume x 0.8)  
clip = clip.volumex(0.8)  
    
# Generate a text clip  
text = (TextClip("asdasda",color='white').set_pos((20,20)))
    
# setting position of text in the center and duration will be 10 seconds  
txt_clip = txt_clip.set_pos('center').set_duration(10)  
    
# Overlay the text clip on the first video clip  
video = CompositeVideoClip([clip, txt_clip])  
    
# showing video  
video.ipython_display(width = 280) 

clip.write_videofile("my_new_video.mp4")




#cv save
cap = cv2.VideoCapture('test25.mp4')
file1 = open("recognized"+str(e1)+".txt","r+", encoding='utf-8')
out = cv2.VideoWriter('cam_output_final.avi',cv2.VideoWriter_fourcc('m','p','4','v'), 20, (620, 480))
#out = cv2.VideoWriter('testvideo'+str(e1)+'.avi', cv2.VideoWriter_fourcc(*'mp4'), 25, 
		           #(640,480),True)
while(True): 
		      
		# Capture frames in the video 
		ret, frame = cap.read() 
		  	
		# describe the type of font 
		# to be used. 
		font = cv2.FONT_HERSHEY_SIMPLEX 
		  
		# Use putText() method for 
		# inserting text on video 
		file1.readlines()
		text = "ذهب الطالب الى المدرسة"
		reshaped_text = arabic_reshaper.reshape(text)
		bidi_text = get_display(reshaped_text) 
		fontpath = "arial.ttf" 
		font = ImageFont.truetype(fontpath, 32)
		try:
			img_pil = Image.fromarray(frame)
			draw = ImageDraw.Draw(img_pil)
			draw.text((50, 80),bidi_text, font = font)
			img = np.array(img_pil)
		except Exception as e:
			break 
		# Display the resulting frame 
		cv2.imshow('window_name', img) 
		out.write(img)
		
		# creating 'q' as the quit  
		# button for the video 
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
		  
# release the cap object 
out.release() 
# close all windows 
cv2.destroyAllWindows() 

e1=n-4
videoclip = VideoFileClip("cam_output_final.mp4v")
audioclip = AudioFileClip('converted'+str(e1)+'.wav')

new_audioclip = CompositeAudioClip([videoclip.audio, audioclip])
videoclip.audio = new_audioclip
videoclip.write_videofile("new_filename.mp4")'''