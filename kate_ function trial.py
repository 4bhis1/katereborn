import speech_recognition as sr
import os
import webbrowser
import requests
from bs4 import BeautifulSoup
import pyttsx3
import keyboard
import pyautogui
import socket

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def openyoutube(string):
    
    print(string)
    
    urlforytb="https://www.youtube.com/results?search_query={}".format(string)
    # print(urlforytb)
    #headers={'User-Agent':'Brave/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}

    headers = {
        "content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "DNT": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }

    # Query parameters required to make get request
    queryParams = {
        "pageSize": 32,
        "compSeasons": 274,
        "altIds": True,
        "page": 0,
        "type": "player",
        "id": -1,
        "compSeasonId": 274
    }
    
    ytburl=requests.get(urlforytb,headers=headers).text
    
    soup=BeautifulSoup(ytburl,'lxml')
    # print(soup.prettify())
    
    urldict=[]
    
    codeintring=soup.prettify()
    #print(codeintring)

    for i in range(len(codeintring)):
        if codeintring[i]=='w' and codeintring[i+2]=='t' and codeintring[i+4]=='h' and codeintring[i+5]=='?':
            j=0
    #         print(codeintring[i:i+19])
    #         for k in range(0,40):
    #             if codeintring[i+k]=='"':
    #                 j=k
    #                 break
            urldict.append(codeintring[i:i+19])
        
    print(urldict)
    
    urlofyotuube="https://www.youtube.com/{}".format(urldict[0])+" song"

    webbrowser.open(urlofyotuube)
    
    print(urlofyotuube)

def google_search(question):
    qstn=requests.get("https://www.google.com/search?q={}".format(question)).text
    soup=BeautifulSoup(qstn,'lxml')
    
    return soup.find_all('div',class_="BNeawe")[0].text

def ears(loop):
    
    r1=sr.Recognizer()
    r2=sr.Recognizer()

    try:

        with sr.Microphone() as source:

            print("ears-> speak now")

            print("ears-> Listening...")


            if loop=="inner":
                audio=r1.listen(source,timeout=0.9,phrase_time_limit=5)
            else:
                audio=r1.listen(source,timeout=0.5,phrase_time_limit=2)

    except:

        print("ears-> working...")

    try:
        print("ears-> recognizing....")
        if(loop=="inner"):
            speak("reacognizing")

        
        query=r2.recognize_google(audio, language='en-in').lower()
        print("think to do -> ",query)

        return query

    except:

        print("Speak once again")

        return " "

def checkingname(string):
    nameofkate=["kate","kite","gate","cat","8","ke","state","cake","date","makeup","wakeup","chat","get","hate"]
    for i in nameofkate:
        if i in string:
            return True

    return False


def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        speak("System is online")
        global internet
        internet = True
    except OSError:
        speak("System is offline, please connect to the internet")

is_connected()

while True:
    front=ears("outer")

    print("into the outerloop")
        

    if checkingname(front):
    
        #speak("ready to speak handle the task()")

        speak("Listening")

        task=ears("inner")
        
        task=task.replace("song","music")
        
        print(task)

        if "close" in task and "music":

            print("closing the music")

            keyboard.press_and_release('ctrl+w')

            print("switching keyboard")            
            keyboard.press_and_release('alt+tab')

        elif "music" in task :
            
            songname=""
            
            for i in range(len(task)):
                if task[i]=='m' and task[i+1]=='u' and task[i+2]=='s' and task[i+3]=='i' and task[i+4]=='c':
                    songname=task[i+6:]
                    break

            print(songname)
            try:
                print("Playing")
                openyoutube(songname)
            except:
                print("some error occured")

        elif "time to sleep" in task:

            print("ok switching out from main loop")
            break

        elif "increase" in task and "volume" in task:

            print("Increasing the volume")
            for i in range(5):
                pyautogui.press("volumeup")

        elif "decrease" in task and "volume" in task:

            print("decreasing the volume")
            for i in range(5):
                pyautogui.press("volumedown")
            
            
        else:
            if task!=" ":
                answer=google_search(task)
                print(answer)
                speak(answer)
        
