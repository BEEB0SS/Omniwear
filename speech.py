import speech_recognition as sr
import serial

ser = serial.Serial("/dev/ttyAMA0", 115200)

reader = sr.Recognizer()
mic = sr.Microphone()

print("Start talking...")

while True:
  with mic as source:
    audio = reader.listen(source)
  words = reader.recognize_google(audio)
  print(words)
  ser.write(bytes(words, 'utf-8'))
