import pyttsx3

data = input('Enter the text to convert to speech: ')

engine = pyttsx3.init()
engine.say(data)
engine.runAndWait()