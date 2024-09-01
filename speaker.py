import pyttsx3

def speak_text(text: str): 
    pyttsx3.speak(text)

def save_text(text: str, filename: str):
    engine = pyttsx3.init()
    engine.save_to_file(text, filename)
    engine.runAndWait()