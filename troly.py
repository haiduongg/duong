import speech_recognition
import pyttsx3
from datetime import date,datetime

dw_ear = speech_recognition.Recognizer()
dw_mouth = pyttsx3.init()
dw_brain = ""
while True :
	with speech_recognition.Microphone() as mic:
		print("robot:i'm listening")
		audio = dw_ear.listen(mic)

	print("dw_brain:....")
	try:
		duong = dw_ear.recognize_google(audio)
	except:
		duong = ""
	print("Duong:"+duong)

	if duong == "":
		dw_brain = "i  can't hear you, try again"
	elif  "hello" in duong:
		dw_brain ="hello duong"
	elif  "today" in duong:
		today = date.today()
		dw_brain = today.strftime("%B %d, %Y")
	elif  "time" in duong :
		now = datetime.now()
		dw_brain = now.strftime("%H:%M:%S")
	elif "what's your name" in duong:
		dw_brain = "i'm a dw"
	elif "bye" in duong:
		dw_brain ="bye duong"
		print("dw_brain:"+dw_brain)
		dw_mouth.say(dw_brain)
		dw_mouth.runAndWait()
		break

	else :
		dw_brain = "ok"
	print("dw_brain:"+dw_brain)
	dw_mouth.say(dw_brain)
	dw_mouth.runAndWait()
