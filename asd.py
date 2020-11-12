import speech_recognition as sr 
import moviepy.editor as mp
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from googletrans import Translator, constants
from pprint import pprint


#clip = mp.VideoFileClip(r'y2mate.com - Advanced English Conversation- Vocabulary, Phrasal Verb, Pronunciation_v144P.mp4')
n=0
start_time=0
end_time=100
while True:
	try:
		ffmpeg_extract_subclip("a.mp4", start_time , end_time, targetname="test"+str(n)+".mp4")
		clip = mp.VideoFileClip(r"test"+str(n)+".mp4")
		n+=1
		start_time+=100
		end_time+=100
		clip2 = mp.VideoFileClip(r"test"+str(n-1)+".mp4")
		if clip == clip2:
			break
	except Exception as e:
		print(e)
		break

for i in int(n):
	print(i)
	clip = mp.VideoFileClip(r"test"+str(n)+".mp4")
	clip.audio.write_audiofile(r'converted'+str(n)+'.wav')

translator = Translator()
r = sr.Recognizer()
audio = sr.AudioFile('converted.wav')
with audio as source:
  audio_file = r.record(source, duration=200)
result=r.recognize_google(audio_file)

# translate a spanish text to arabic for instance
translation = translator.translate(result, dest="ar")

with open('recognized.txt',mode ='a', encoding="utf-8") as file: 
   file.write("Recognized Speech:") 
   file.write("\n") 
   file.write(result)
   file.write("\n") 
   file.write(translation.text) 
   print("ready!")


'''
r = sr.Recognizer()
audio = sr.AudioFile("converted.wav")

with audio as source:
  audio_file = r.record(source)

result = r.recognize_google(audio_file)

# exporting the result 
with open('recognized.txt',mode ='w') as file: 
   file.write("Recognized Speech:") 
   file.write("n") 
   file.write(result) 
   print("ready!")

 '''