import speech_recognition as sr

def listen_for_speech(react_msg: str):
    # Take audio from the microphone
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print(react_msg)
        audio = r.listen(source)

    # Print the audio as text
    try:
        speech = r.recognize_sphinx(audio)
        return speech
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))