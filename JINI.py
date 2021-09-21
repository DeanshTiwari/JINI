from PyQt5 import QtWidgets, uic,QtCore
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from uic import loadUiType
import pyttsx3
import speech_recognition as sr
import sys
import os
import time
import webbrowser
import datetime
import wikipedia
import pywhatkit
import pyjokes
import random

flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    intro = "My name is jini,How may i help you"
    if hour >= 0 and hour < 12:
        speak("Good morning" + intro)
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + intro)
    else:
        speak("Good night" + intro)


class mainT(QThread):
    def __init__(self):
        super(mainT, self).__init__()

    def run(self):
        self.JARVIS()

    def STT(self):
        r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listning...........")
    audio = r.listen(source)
    try:
        print("Recog......")
    text = sr.recognize_google(audio, language='en-in')
    print(">> ", text)
    except Exception:
        speak("Sorry Speak Again")
    return "None"
    text = text.lower()
    return text

    def JARVIS(self):
        wishme()

    while True:
        self.query = self.STT()
    if 'open google' in self.query:
        speak("opening...")
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
        webbrowser.get(chrome_path).open("google.com")
    elif 'open youtube' in self.query:
        speak("opening...")
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
        webbrowser.get(chrome_path).open("youtube.com")
    elif 'open a k t u' in self.query:
         speak("opening A.K.T.U website")
         chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
         webbrowser.get(chrome_path).open("https://aktu.ac.in/")
    elif 'open stack overflow' in self.query:
         webbrowser.open("stackoverflow.com")
         speak("opening stackoverflow...")
    elif 'open github' in self.query:
        webbrowser.open("https://www.github.com")
        speak("opening github")
    elif 'open facebook' in self.query:
        webbrowser.open("https://www.facebook.com")
        speak("opening facebook")
    elif 'open instagram' in self.query:
        webbrowser.open("https://www.instagram.com")
        speak("opening instagram")
    elif 'open google' in self.query:
        webbrowser.open("https://www.google.com")
        speak("opening google")
    elif 'open yahoo' in self.query:
        webbrowser.open("https://www.yahoo.com")
        speak("opening yahoo")
    elif 'open gmail' in self.query:
        webbrowser.open("https://mail.google.com")
        speak("opening google mail")
    elif 'open snapdeal' in self.query:
        webbrowser.open("https://www.snapdeal.com")
        speak("opening snapdeal")
    elif 'open amazon' in self.query or 'shop online' in self.query:
        webbrowser.open("https://www.amazon.com")
        speak("opening amazon")
    elif 'open flipkart' in self.query:
        webbrowser.open("https://www.flipkart.com")
        speak("opening flipkart")
    elif 'open ebay' in self.query:
        webbrowser.open("https://www.ebay.com")
        speak("opening ebay")
    elif 'who is' in self.query:
        speak("Searching...!")
        result = wikipedia.summary(self.query, sentences=2)
        print(result)
        speak("Acording To Wikipedia" + result)
    elif 'what is' in self.query:
        speak("Searching...!")
        result = wikipedia.summary(self.command, sentences=2)
        speak("Acording To Wikipedia" + result)
    elif 'play' in self.query:
        song = self.query.replace("play", "")
        speak("playing....!")
        pywhatkit.playonyt(song)
    elif "tell me the time" in self.query:
        time = datetime.datetime.now()
        speak("current time is" + time.strftime("%I" + "hour" + "%M"))
    elif "tell me the date" in self.query:
        time = datetime.datetime.now()
        speak("today is" + time.strftime("%d" + "%B" + "%Y"))
    elif "tell me a joke" in self.query:
        speak(pyjokes.get_joke())
    elif "open sublime" in self.query:
        speak("opening...")
        path = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
        os.startfile(path)
    elif "open powerpoint" in self.query:
        speak("opening...")
        path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office"
        os.startfile(path)

    elif 'who make you' in self.query or 'who created you' in self.query or 'who  develop you' in self.query:
        ans_m = " For your information Devansh Tiwari created me !"
        print(ans_m)
        speak(ans_m)
    elif "tell me something about yourself" in self.query or "who are you" in self.query \
         or "your details" in self.query:
        about = "I am Jini an A I based virtual assistant and i can help you lot  like a your close friend !"
        print(about)
        speak(about)
    elif "like what" in self.query:
        help = "i can open specific website for u,i can play music online," +  "i can open appliction,i can tell you date and time " +  "and even entertain u by cracking some funnny joke "
        print(help)
        speak(help)
    elif "hello" in self.query or "hello Jarvis" in self.query:
        hel = "Hello Devansh Sir ! How May i Help you.."
        print(hel)
        speak(hel)
    elif "your feeling" in self.query:
        print("feeling Very good after meeting with you")
        speak("feeling Very good after meeting with you")

    elif "bye" in self.query:
        speak("ok good bye,have a nice day")
        exit()
FROM_MAIN, _ = loadUiType(os.path.join(os.path.dirname(__file__), "./scifi.ui"))


class Main(QMainWindow, FROM_MAIN):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

    self.setupUi(self)
    self.setFixedSize(1920, 1080)
    self.label_7 = QLabel
    self.exitB.setStyleSheet("background-image:url(./lib/exit - Copy.png);\n"  "border:none;")
    self.exitB.clicked.connect(self.close)
    self.setWindowFlags(flags)
    Dspeak = mainT()
    self.label_7 = QMovie("./lib/gifloader.gif", QByteArray(), self)
    self.label_7.setCacheMode(QMovie.CacheAll)
    self.label_4.setMovie(self.label_7)
    self.label_7.start()
    self.ts = time.strftime("%A, %d %B")
    Dspeak.start()
    self.label.setPixmap(QPixmap("./lib/tuse.png"))
    self.label_5.setText("<font size=8 color='white'>" + self.ts + "</font>")
    self.label_5.setFont(QFont(QFont('Acens', 8)))


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())
