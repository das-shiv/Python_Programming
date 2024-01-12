def speak(func):
    text = func("Hello")
    print(text)

def loud(mssg):
    return mssg.upper()

def quiet(mssg):
    return mssg.lower()


speak(loud)
speak(quiet)