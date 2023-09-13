def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == '__main__':
    import requests
    import json
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=04bda2ce2f0f40598adeec2fbab8a707"
    news = requests.get(url).text            # converts into dictionary
    news_py = json.loads(news)               # makes it python readable
    art = news_py["articles"]
    speak("Today's news headlines are as follows")
    for articles in art:
        speak(articles["title"])
        speak("next headline")
