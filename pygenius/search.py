import urllib2
import json
import re
import difflib

def search_song(title):
    title = re.sub(' ', '-', title)
    search_result = urllib2.urlopen(
        "http://api.rapgenius.com/search?q=" + str(title)
        ).read()
    data = json.loads(search_result)
    greatest = 0
    sim_title = ""
    for i in data["response"]["hits"]:
        sim = difflib.SequenceMatcher(a=title.lower(),b=i["result"]["title"].lower()).ratio()
        if(sim >= greatest):
                sim_title = i["result"]["title"]
                greatest = sim
    return sim_title
