
    elif 'tell me about' in command: 
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 3)
        print(info)