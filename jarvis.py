# virtualenv jarvis
# activate 
# pip3 install pyttsx3
# pip3 install wikipedia

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    print(time)
    #speak('The current time is: ' + time)

def wiki():
    query = "Iphone"
    results = wikipedia.summary(query, sentences=2)
    print("According to wikipedia")
    print(results)
    speak("According to wikipedia")
    speak(results)

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language= 'en-US')
        print('Your said: ' + query)
    except Exception as e:
        print(e)    

speak('Welcome back')
time()
wiki()
takecommand()