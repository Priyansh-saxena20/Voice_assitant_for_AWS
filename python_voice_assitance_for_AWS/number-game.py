import random
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)   # here you can change voice

def speak(audio):
    '''
    This function let your AI to speak
    '''
    engine.say(audio)
    engine.runAndWait()

n = random.randint(1, 100)
guess = 1

while (guess <= 6):
    i = int(input("Enter Your Guess: "))

    if (i < n):
        speak("Your guess is smaller than the number.")
    elif (i > n):
        speak("Your guess is greater than the number.")
    else:
        speak("YOU WON!")
        print("You took", guess, "guesses")
        break
    speak(f"You have {6-guess} guesses left")
    guess = guess+1

if (guess > 6):
    print(f"GAME OVER the number was {n}")
