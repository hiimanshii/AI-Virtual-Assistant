import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import time
import random
import wolframalpha
import json
import requests
import pyjokes
import smtplib
import psutil
from GoogleNews import GoogleNews


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def online():
    speak("Hello ma'am")
    speak("starting all system application")
    speak("installing all drivers")
    os.system('C:\\Users\\hp\\elegant_theme_1_1_by_chinni1991_d6efsiy.rmskin ')
    speak("every driver is installed")
    speak("all system have been started")
    speak("I am online ma'am ")

def gooffline():
    speak("ok ma'am")
    speak("closing all systems")
    speak("disconnecting to severs")
    speak("going offline")
    quit()


def shutdown():
    speak("understood ma'am")
    speak("your pc will shutdown in 10 seconds")
    speak("connecting to command prompt")
    speak("shutting down your computer")
    os.system("shutdown -s")


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('himanshigupta286@gamail.com', 'hima@8576')
    server.sendmail('himanshiguptariya@gmail.com', to, content)
    server.close()

def jokes():
    speak(pyjokes.get_jokes())


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at " + usage)
    battery = psutil.sensors_battery()
    speak("The battery is at ")
    speak(battery.percent)



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon! ")
    else:
        speak("Good evening!")

    speak("I am ALEX !")


def takeCommand():
    # it takes microphone input from the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user: {query}\n")


    except Exception as e:
        # print(e)

        print("say that again please....")
        return "None"
    return query


def google_news():
    googlenews = GoogleNews()
    googlenews = GoogleNews(lang='en')
    speak("do you have a specific topic in mind??")
    text = takecommand()
    while (text == "ERROR" or "ok go back" in text):
        if ("ok go back" in text):
            return
        speak("sorry let's try again")
        speak("do you have a specific topic in mind??")
        text = takecommand()
        continue
    if text == "no":
        googlenews.search('india')
    else:
        googlenews.search(text)

    while (True):
        news = googlenews.result()
        for i in range(0, len(news)):
            print("title = " + news[i]['title'])
            print("media = " + news[i]['media'])
            print("date = " + news[i]['date'])
            print("link = " + news[i]['link'])
            speak(news[i]['title'])
            speak(news[i]['desc'])
            print("\n\n")
        speak("would you like to hear more??")
        text = takecommand()
        if ("no" in text):
            speak("ok duely noted")
            break
        googlenews.clear()
        googlenews.getpage(2)


'''def media():
    speak("ok ma'am")
    speak("starting required application")
    speak("what do you want me to play for you")
    l=takeCommand()
    speak("ok ma'am I am playing for you")
    music_dir = 'C:\\users\\hp\\music'
    songs = os.listdir(music_dir)
    print(songs)
    os.startfile(os.path.join(music_dir,songs[3]))'''

if __name__ == "__main__":
    wishMe()
    online()

    # speak("Hello Himanshi!")
    while True:
        speak("How may i help you ma'am?")
        query = takeCommand().lower()
        if query == 0:
            continue

        # logic for executing tasks based query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C:\\users\\hp\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[3]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is{strTime}")

        elif 'open code' in query:
            codePath = os.dirname('C:\\Users\\hp\\Desktop\\software\\PyCharm Community Edition 2020.2.2\\bin\\pycharm64.exe')
            os.startfile(codePath)

        elif 'who are you' in query or 'what can you do' in query:
            speak('''hello ma'am,I am Alex version 1 point O your persoanl assistant. I am programmed to do several tasks like
                  opening youtube,google chrome,gmail  ,predict time,take a photo,search wikipedia,predict weather
                  in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!''')

        elif query == "Alex":
            online()

        elif query == 'shutdown':
            shutdown()

        elif query == "offline":
            gooffline()

        elif 'restart' in query:
            os.system("shutdown -r")

        elif query in ['hi alex', 'hey alex', 'hello ', 'whatsup', 'sup', 'good']:
            a = random.choice(["hi ma'am", "hello ma'am"])
            speak(a)

        elif 'find' in query:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question = takeCommand()
            app_id ="X7589Q-GY6UK2GKVA"
            client = wolframalpha.Client('X7589Q-GY6UK2GKVA')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            speak("I was built by Himanshi")
            print("I was built by Himanshi")

        elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif 'date' in query:
            date()

        elif 'send email' in query:
            try:
                speak("What should I send?")
                content = takeCommand()
                to = "himanshiguptariyar@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Unable to send email")

        elif 'battery percentage' in query:
            cpu()

        elif 'joke' in query:
            jokes()

        elif "weather" in query:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name = takeCommand()
            complete_url = base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"]!="404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")


time.sleep(3)