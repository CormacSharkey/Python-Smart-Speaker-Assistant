import listener as ls
import speaker as sp
import datetime as dt
import human_readable as hr

nametag = "Sherlock"

def eventLoop():
    while True:
        speech = ls.listen_for_speech("listening for you...", "whisper")

        if speech != None and nametag.casefold() in speech:
            if "what time is it" in speech:
                current_time = dt.datetime.now()
                sp.speak_text("It is " + hr.timing(current_time, formal=False) + ".")

    