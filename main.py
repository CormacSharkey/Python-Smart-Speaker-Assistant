# NOTE: this example requires PyAudio because it uses the Microphone class

import listener



if __name__ == "__main__":
    print(listener.listen_for_speech("listening to you..."))