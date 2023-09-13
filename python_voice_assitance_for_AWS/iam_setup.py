import boto3
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)   # here you can change voice

def speak(audio):
    '''
    This function let your AI to speak
    '''
    engine.say(audio)
    engine.runAndWait()
    
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

iam = boto3.client('iam')

speak("What will be the username")
username = takeCommand().lower()

iam.create_user(
    UserName = username
)

iam.attach_user_policy(
    PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess',
    UserName=username,
)

response = iam.create_access_key(
    UserName=username
)

print(f'Your access key id is {response["AccessKey"]["AccessKeyId"]}\nYour access key secret is {response["AccessKey"]["SecretAccessKey"]}')
