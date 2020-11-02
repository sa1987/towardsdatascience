# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 01:39:32 2020

#Testing gTTS python module and play audio with os module and playsound module

@author: 19240179
"""
#pip install gTTS
from gtts import gTTS
import os
from playsound import playsound

text = "Hello! I am testing gTTS module."
tts = gTTS(text)
tts.save("Hello.mp3")
#if you want to play it using OS module
os.system("Hello.mp3")

inputText=input("Enter your text: ")
tts = gTTS(inputText)
tts.save("Helloinput.mp3")
playsound("Helloinput.mp3")

