import urllib2
import json

def get_song_data(id):
    json_data = urllib2.urlopen("http://api.rapgenius.com/songs/" + str(id))
    data = json.loads(json_data.read())
    return data

def get_song_lyrics(data):
    lyrics = []
    for i in data["response"]["song"]["lyrics"]["dom"]["children"][0]["children"]:
        try:
            for x in range(0, len(i["children"]), 2):
                lyrics.append(json.dumps(i["children"][x])[1:-1])
        except TypeError:
            tmp = ""
        except KeyError:
            tmp =""
    return lyrics

def get_prim_artist(data):
    return json.dumps(data["response"]["song"]["primary_artist"]["name"])[1:-1]


