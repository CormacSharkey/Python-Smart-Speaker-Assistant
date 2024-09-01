import time
import listener
import speaker



if __name__ == "__main__":
    # print(listener.listen_for_speech("listening to you..."))

    speech = listener.listen_for_speech("listening to you...", "Google")

    print(speech)

    speaker.speak_text(speech)

    speaker.speak_text("We out here walking, like back in the old days.")