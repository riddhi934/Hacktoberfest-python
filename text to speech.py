# This code will convert your text to speech.

import pyttsx3
engine = pyttsx3.init()
def converter(text):
    engine.say(text)
    engine.runAndWait()
text = input('ENTER THE TEXT :')
converter(text)
