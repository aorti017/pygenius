import urllib2
import json
import re

def search_song(title):
    title = re.sub(' ', '-', title)
    search_result = urllib2.urlopen(
        "http://api.rapgenius.com/search?q=" + str(title)
        ).read()
    data = json.loads(search_result)
    results = {}
    for i in data["response"]["hits"]:
        results[i["result"]["title"]] = i["result"]["id"]
    return results

