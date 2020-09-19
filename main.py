#!/usr/bin/python3
"""
main module for KARA AI
dep: 
speech_recognition module
pyaudi
gtts
"""
from time import ctime
import speech_recognition as sr
import webbrowser
import time
import os
import playsound
import random
from gtts import gTTS


r = sr.Recognizer()
def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            kara_speak(ask)
        audio = r.listen(source)
        voice_data =""
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            kara_speak(" Sorry I didn't understand")
        except sr.RequestError:
            kara_speak("Sorry, i'm speeling")
        return voice_data

def kara_speak(audio):
    tts = gTTS(text=audio, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + 'mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio)
    os.remove(audio_file)


def respond(voice_data):
    if 'hello' in voice_data:
        kara_speak("Hello master")
    if 'what time is it' in voice_data:
        kara_speak(ctime())
    if 'search' in voice_data:
        search = record("What do want to search for?")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
    if 'exit' in voice_data:
        exit()
time.sleep(1)
kara_speak("How can I help you")

while True:
    my_audio =  record()
    print(respond(my_audio))
