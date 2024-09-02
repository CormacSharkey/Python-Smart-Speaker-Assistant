# Python-Smart-Speaker-Assistant

## _An AI Voice Assistant, Written in Python_

[This is how to add a comment]: # 

This project has three main components: the **listener**, the **speaker**, and the **assistant**.

## Listener 
[listener.py](listener.py)
The Listener takes speech audio from a connected microphone and returns the text as a string.
It contains the following functions:
- **listen_for_speech(_react_msg_: str, _model_=None)**


## Speaker 
[speaker.py](speaker.py)
The speaker takes a text string and returns speech audio of the given text.
It contains the following functions:
- **speak_text(_text_: str)**
- **save_text(_text_: str, _filename_: str)**


## Assistant 
[assistant.py](assistant.py)
The assistant runs the main event loop, which calls on the listener for spoken commands and uses the speaker to respond with speech.
- **nametag**: _used as the trigger for the assistant to accept commands_