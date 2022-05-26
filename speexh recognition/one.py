import speech_recognition as sr

r1=sr.Recognizer()
r2=sr.Recognizer()


with sr.Microphone() as source:

    print("speak now")

    print("Listening...")

    audio=r1.listen(source,timeout=0.9,phrase_time_limit=5)

print("recognizing....")
print(r2.recognize_google(audio, language='en-in'))
