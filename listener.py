import speech_recognition as sr

def listen_for_speech(react_msg: str, model=None):
    # Take audio from the microphone
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print(react_msg)
        audio = r.listen(source)

    # Use Whisper if specified
    if model != None and "whisper" in model.casefold():
        print("Using OpenAI's Whisper as the model...")

        # recognize speech using whisper
        try:
            speech = r.recognize_whisper(audio, model="tiny", language="english")
            return speech
        except sr.UnknownValueError:
            print("Whisper could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Whisper; {e}")

    # Use Google Speech Recognition if specified
    elif model != None and "google" in model.casefold():
        print("Using Google Speech Recognition as the model...")

        # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            speech = r.recognize_google(audio)
            return speech
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    # Use PocketSphinx as the default
    else:
        print("Using PocketSphinx as the model...")

        # Print the audio as text
        try:
            speech = r.recognize_sphinx(audio)
            return speech
        except sr.UnknownValueError:
            print("PocketSphinx could not understand audio")
        except sr.RequestError as e:
            print("PocketSphinx error; {0}".format(e))
