import speech_recognition as sr

reader = sr.Recognizer()
mic = sr.Microphone()

print("Start talking...")

while True:
  with mic as source:
    audio = reader.listen(source)
  words = reader.recognize_google(audio)
  print(words)
