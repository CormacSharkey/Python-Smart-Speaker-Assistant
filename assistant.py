import listener as ls
import speaker as sp
import datetime as dt
from youtube_search import YoutubeSearch
import human_readable as hr

nametag = "Sherlock"

def eventLoop():
    while True:
        speech = ls.listen_for_speech("listening for you...", "whisper")

        if speech != None and nametag.casefold() in speech:
            if "what time is it" in speech:
                current_time = dt.datetime.now()
                sp.speak_text("It is " + hr.timing(current_time, formal=False) + ".")
            elif "Youtube".casefold() in speech:
                query = speech.replace(r"Play ".casefold(), '').replace(r" on Youtube".casefold(), '')
                result = youtube_search(query)







def youtube_search(query):
    result = YoutubeSearch(query, max_results=1).to_dict()
    result_url = result.get("title"), "https://www.youtube.com" + result.get("url_suffix")

    return result_url

def youtube_play(query):
    print("Hello")