
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # Select a female voice (change the index if needed)
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    print("Welcome to Robo Speaker created by Neha Gurung")
    y = "Welcome to Robo Speaker created by NG"
    speak({y})
    while True:

        x = input("Enter what you want me to speak : ")
        if x == "q":
            z = " You are taking exit"
            speak({z})
            break

        speak({x})

