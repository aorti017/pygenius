import urllib2
import json
import re
import difflib
import song

def search_song(title):
    title = re.sub(' ', '-', title)
    search_result = urllib2.urlopen(
        "http://api.rapgenius.com/search?q=" + str(title)
        ).read()
    data = json.loads(search_result)
    greatest = 0
    sim_id = -1
    for i in data["response"]["hits"]:
        sim = difflib.SequenceMatcher(a=title.lower(),b=i["result"]["title"].lower()).ratio()
        if(sim >= greatest):
                sim_id = i["result"]["id"]
                greatest = sim
    return song.song(sim_id)
