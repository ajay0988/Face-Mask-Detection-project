#!/usr/bin/env python
# coding: utf-8

# In[1]:


import speech_recognition as sr
import pyttsx3

#changing voice 
engine=pyttsx3.init()
voice=engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)

#connecting microphone to device
def speak():
    with sr.Microphone() as source:
        r=sr.Recognizer()
        pyttsx3.speak("tell your command name:")
        sound=r.listen(source)
        pyttsx3.speak("i got it, please wait....")
        Text=r.recognize_google(sound)
    return Text 

