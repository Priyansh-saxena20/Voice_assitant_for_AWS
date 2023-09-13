 import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyaudio
import random
import pywhatkit
import pyjokes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)   # here you can change voice

def speak(audio):
    '''
    This function let your AI to speak
    '''
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    '''
    this function wishes you
    '''
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis! How may I help you.")


def takeCommand():
    '''
    this function will take voice command from user
    and returns string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1   # this will help user to take 1 sec pause so that AI will not complete the voice in middle
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print("user said:", query)
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "none"
    return query

if __name__ == "__main__":
   wishMe()
   while True:
        query= takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences= 2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'D:\\alice isnt dead'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[random.randint(0, 4)]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        
        elif 'open code' in query:
            code_path = "C:\\Users\\HP\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif 'play' in query:
            try:
                song = query.replace("play", "")
                print("playing"+song)
                speak("playing")
                pywhatkit.playonyt(song)
            except Exception as e:
                speak("sorry I was not able to recognise that. Can you say that again?")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'weather' in query:
            os.system("python weather.py")
            
        elif 'launch ec2' in query:
            os.system('python ec2_launch.py')
            speak("EC2 instance launched successfully")
        
        elif 'news' in query:
            os.system('python news.py')
        
        elif 'setup iam user' in query:
            os.system('python iam_setup.py')
            speak("user created")
        
        elif 'play a game' in query:
            os.system('python multiplayer_game.py')
        
        elif 'bulk email' in query or 'bulk mail' in query:
            os.system('python ./LW/email_service.py')
            speak('Email sent successfully')
        
        elif 'email to team' in query:
            os.system('python team_email.py')
            speak('Email sent successfully')
        
        elif 'click a photo' in query or 'click photo' in query or 'capture photo' in query: 
            os.system('python photo.py')
        
        elif 'bored' in query:
            speak("okay let's play a game, guess the number I am thinking")
            os.system('python number_game.py')
        
        elif 'create a bucket' in query:
            os.system('python create_s3_bucket.py')
            speak('bucket created')

        elif 'exit' in query:
            print("Shutting down jarvis...")
            speak("Going to sleep.")
            break
