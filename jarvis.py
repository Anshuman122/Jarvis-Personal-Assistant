import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices' , voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to convert voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("taking your command sir.....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=6, phrase_time_limit=10)

    try:
        print("understanding your command....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("say that again please...")
        return "none"
    return query

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good Morning Master Anshuman")
    elif hour>12 and hour<18:
        speak("Good Afternoon Anshuman Sir")
    else:
        speak("Good Evening")
    speak("I am your jarvis Sir. Please Tell me what are todays task")

#to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email id', 'your password')
    server.sendmail('your email id', to, content)
    server.close()

if __name__ == "__main__":
    wish()
    while True:

        query = takecommand().lower()

        #logic building for tasks

        if "open notepad" in query:
            npath = "C:\\Windows\\SysWOW64\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "C:\\Users\\akn\\Videos\\pendrive data\\music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif " ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is{ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open geeksforgeeks" in query:
            webbrowser.open("www.geeksforgeeks.org")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.in")

        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "play songs on youtube" in query:
            speak("which song should i play on youtube?")
            SP = takecommand().lower()
            kit.playonyt(f"{SP}")

        elif "send email" in query:
            try:
                speak("what should i type?")
                content = takecommand().lower()
                to = "anamika1621@gmail.com"
                sendEmail(to,content)
                speak("email has been sent")

            except Exception as e:
                print(e)
                speak("sorry i am not able to send this mail")

        elif "go to sleep" in query:
            speak("thanks for using me,sir. have a good day")
            sys.exit()
