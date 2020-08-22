import pyttsx3
import os

pyttsx3.speak("Welcome")
pyttsx3.speak("This is your personal system assistant, Enter the application you want to run on your system")


while True:
    p = input("chat with me with your requirements : ")

    if ((("run" in p) or ("open" in p )) and ("chrome" in p)) :
        pyttsx3.speak("Opening Chrome")
        os.system("chrome")

    elif (("run" in p) or  ("open" in p )) and (("notepad" in p) or ("editor" in p) ) :
        pyttsx3.speak("Opening Notepad")
        os.system("notepad")

    elif ('facebook' in p):
        pyttsx3.speak('opening facebook')
        os.system('start  http://www.facebook.com/')

    elif ('notepad++' in p) or ('pad editor' in p):
        pyttsx3.speak('Launching your notepad++')
        os.system('notepad++')

    elif (("run" in p) or  ("open" in p ))  and ("player" in p) and ("media" in p) :
        pyttsx3.speak("Opening Media Player")
        os.system("wmplayer")

    elif ("exit" in p)  or ("quit" in p):
        break

    else:
        print("dont support")