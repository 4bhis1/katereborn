import pyttsx3
import datetime
import socket
import win32api,win32con
import speech_recognition as sr


def ears(loop):
    
    r1=sr.Recognizer()
    r2=sr.Recognizer()

    try:

        with sr.Microphone() as source:

            print("ears-> speak now")

            print("ears-> Listening...")

            audio=r1.listen(source,timeout=0.5,phrase_time_limit=1)

    except:

        print("ears-> working...")

    try:
        print("ears-> recognizing....")

        #if(loop=="inner"):
            #speak("reacognizing")

        
        query=r2.recognize_google(audio, language='en-in').lower()
        print("think to do -> ",query)

        return query

    except:

        print("Speak once again")

        return " "

print("jai mata di")
print(ears("inner"))
