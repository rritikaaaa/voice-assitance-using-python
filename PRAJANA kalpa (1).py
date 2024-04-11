#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import speech_recognition as sr
import pyttsx3
import pywhatkit #play video on youtube
import datetime #for date and time
import wikipedia #for searching info
import webbrowser #already in built to browse
import os #interface
import pyjokes #for jokes
import subprocess
import cv2#install open cv.python
import requests
from bs4 import BeautifulSoup
import phonenumbers



# FOR WISHING
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        talk("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        talk("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        talk("Hello,Good Evening")
        print("Hello,Good Evening")

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

# KALPA WILL SPEAK THE RESULT
def talk(text):
    engine.say(text)
    engine.runAndWait()

wishMe()
engine.say('i am prajana kalpa you can call me kalpa')
engine.say('how may i help u')
engine.runAndWait()



# TAKING USERS SEVICES

def take_command():
    try:
        with sr.Microphone() as source:
            print("say something")
            engine.say("say something")
            engine.runAndWait()
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'kalpa' in command:
                talk(command)
               # print(command)
                
    except:
        print("sorry")
    return command


        
def run_kalpa():
    command = take_command()
    
# TO PLAY VIDEOS ON YOUTUBE
    if 'play' in command:
        video = command
        talk(command)
        print('playing')
        pywhatkit.playonyt(video)       #LIBRARY TO PLAY ON YOUTUBE
        
# TIMING       
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%p')
        talk(time)
        print(time)
                  
#CODE FOR SEARCHING WIKIPEDIA         
    elif 'who is' in command:
        person = command
        info = wikipedia.summary(person ,3)
        talk("according to wikipedia")
        print(info)
        talk(info)
    elif 'what is' in command:
        person = command
        info = wikipedia.summary(person ,1)
        talk("according to wikipedia")
        print(info)
        talk(info)
    elif 'tell' in command:
        person = command
        info = wikipedia.summary(person ,1)
        talk("according to wikipedia")
        print(info)
        talk(info)
    elif 'recipe' in command:
        person = command
        info = wikipedia.summary(person ,1)
        talk("according to wikipedia")
        print(info)
        talk(info)
  # pywebbrowser code for browsing      
    
    elif 'open youtube' in command:
        webbrowser.open('youtube.com')
    
    elif 'open google' in command:
        webbrowser.open('google.com')
    
    elif 'search'  in command:
            command = command.replace("search", "")
            webbrowser.open_new_tab(command)
    
    elif 'open google'  in command:
        talk("what should i search for you in google")
        cm = take_command().lower()
        webbrowser.open("{cm}")
    
    elif 'news' in command:
        talk("todays news is")
        webbrowser.open('inshorts.com')
                        
    
        
#pyos for interface
    
   
        
    
    elif 'open microsoft teams' in command:
        try:
            teamspath = 'C:\\Users\\ritika\\AppData\\Local\\Microsoft\\Teams'
            os.startfile(teamspath)
        except Exception as e:
            print(e)
            talk("sorry")
        
    elif 'open projectpresentation' in command:
        try:
            teamspath = 'C:\\Users\\ritika\\OneDrive\\Documents\\projectpresentation.pptx'
            os.startfile(teamspath)
        except:
            talk(sorry)
    elif 'open commandprompt' in command:
         os.system('start cmd')
    elif 'open cammera'in command:
        cap = cv2.videoCapture(0)
        while True:
            ret,img = cap.read()
            cv2.inshow('webcam',img)
            k=cv2.waitKey(50)
            if k==27:
                break;
            cap.release()
            cv2.destroyAllWindows()
        
        
        
        
    elif "log off" in command or "sign out" in command:
        try:
            talk("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
        except exception as e:
            print(e)
            talk(sorry)
    
 # pyjokes for jokes
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    
# NORMAL CONVERSATION      
    elif 'good kalpa' in command:
        engine.say('thank you')
        engine.runAndWait()
        
    elif 'who are you' in command or 'what can you do' in command:
            talk('I am PRAJANA KALPA your personal assistant. I am programmed to minor tasks like' 
                  'opening youtube,google chrome, gmail and stackoverflow ,predict time,search wikipedia,  get top headline news from inshorts ')
   
   
    elif "ip address" in command:
        ip = get('https://api.ipify.org').text
        talk(f"your ip address is {ip}")
        print(ip)
        
    elif " temperature" in command:
        search ="temperature in bhilai"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div",class_="BNeawe").text
        talk(f"current {search} is {temp}")
        
run_kalpa()
        
        
        
        


# In[4]:





def talk():
    engine.say(text)
    engine.runAndWait()
    


# In[10]:


def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        talk("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        talk("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        talk("Hello,Good Evening")
        print("Hello,Good Evening")
        


# In[ ]:


import ecapture as ec
ec.capture(0,"test","img.jpg")


# In[ ]:


import os
 
print(os.name)


# In[ ]:


import cv2

cap = cv2.VideoCapture(1)
while True:
    ret,frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == ord('q'):
        break
                
cap.release()
cv2.destroyAllWindows()


# In[ ]:




