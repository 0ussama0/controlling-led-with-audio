import pyfirmata2
import time
import speech_recognition as sr 
import pyaudio
import pywhatkit

from gtts import gTTS


board = pyfirmata2.Arduino("COM4")
ledpin = board.get_pin("d:3:o")
while True:
    print("rec..")
    l = sr.Recognizer()
    with sr.Microphone() as mic:
        voice = l.listen(mic)
        com = l.recognize_google(voice)
        com = com.lower()

        print(com)

        if ("computer") in com :
           
            if com=="computer on":
                ledpin.write(1)
            elif com=="computer off":
                ledpin.write(0)
            elif com=="computer exit":
                break
            else:
                print("try again")
board.exit()