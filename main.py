import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes




# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

listener = sr.Recognizer()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command(timeout = 5, phrase_time_limit=5):
    command = ""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source, timeout = timeout, phrase_time_limit=phrase_time_limit)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            if 'kevin' in command:
                command = command.replace('kevin', '') 
    
    except sr.UnknownValueError:
        print("Sorry, I did not understand that")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    return command



def run_kevin():
    command = take_command()
    if command:
        if 'play' in command:
            song = command.replace('play', '')
            talk(f'Playing {song}')
            pywhatkit.playonyt(song)
        elif 'how are you' in command:
            response = "I am good, thank you for asking. I hope you're doing well too. If I can help with anything, just ask."
            print(response)
            talk(response)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk(f'Current time is {time}')
        elif 'date' in command:
            date = datetime.datetime.now().strftime('%Y-%m-%d')
            print(date)
            talk(f'Today\'s date is {date}')
        elif 'tell me about' in command:
            person = command.replace('tell me about', '')
            try:
                info = wikipedia.summary(person, sentences=3)
                print(info)
                talk(info)
            except wikipedia.exceptions.DisambiguationError as e:
                print(f"Disambiguation error: {str(e)}")
                talk("There are multiple results for this topic, please be more specific.")
            except wikipedia.exceptions.PageError:
                print("Page not found")
                talk("I couldn't find any information on that topic.")
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                talk("Sorry, I couldn't retrieve the information.")
        elif 'what is your name' in command:
            response = 'My name is Kevin. My mission is to assist you.'
            print(response)
            talk(response)
        elif 'are you single' in command:
            response = 'I am in a relationship with Wi-Fi.'
            print(response)
            talk(response)
        elif 'joke' in command:
            joke = pyjokes.get_joke()
            print(joke)
            talk(joke)
        else:
            error_message = "I did not get that, but I am going  to search it for you!"
            print(error_message)
            talk(error_message)
            pywhatkit.search(command)
    else:
        print("No command received.")

while True:
    run_kevin()
