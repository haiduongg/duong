import speech_recognition

dw_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
	print("robot:i'm listening")
	audio = dw_ear.listen(mic)
try:
	duong = dw_ear.recognize_google(audio)
except:
	duong = ""
print(duong)
