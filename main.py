import speech_recognition as sr;
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()

# change the voice male to female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    # engine.say('Hi, I am kevin')
    engine.say(text)
    engine.runAndWait()

def talk_command():
    try:  
        with sr.Microphone() as source:
            print("listening.....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'kevin' in command:
                command = command.replace('kevin', '')
                print(command)

    except:
        pass
    return command


def run_kevin():
    command = talk_command()
    print(command)
    if 'play' in command: 
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'how are you' in command: 
        print("I am good, thank you for asking. I hope you're doing well too. If I can help with anything, just  ask.")
        talk("I am good, thank you for asking. I hope you're doing well too. If I can help with anything, just  ask.")

    
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)
    
    elif 'date' in command:
        date = datetime.datetime.now().date()
        print(date)
        talk(date)

    elif 'tell me about' in command: 
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)
    
    elif 'what is your name' in command:
        print('My name is kevin. My mission is To assist you.')
        talk('My name is kevin. My mission is To assist you.')

    elif 'are you single' in command: 
        talk('I am in a relationship with wifi')
        
    elif 'jokes' in command:
        jokes = pyjokes.get_joke()
        print(jokes)
        talk(jokes)
    else: 
        talk('I did not get it but I am going to search it for you')
        pywhatkit.search(command)

while True:
    run_kevin()