#!/usr/bin/python3
"""
main module for KARA AI
dep: 
speech_recognition module
pyaudi
gtts
"""

import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    print("say something")
    audio = r.listen(source)
    voice_data = r.recognize_google(audio)
    print(voice_data)
