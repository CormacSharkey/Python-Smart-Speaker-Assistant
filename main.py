# NOTE: this example requires PyAudio because it uses the Microphone class


import time
import listener
import speaker



if __name__ == "__main__":
    # print(listener.listen_for_speech("listening to you..."))

    speaker.speak_text("We out here walking, like back in the old days.")