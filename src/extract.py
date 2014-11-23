import urllib2
import json

def get_song_data(id):
    json_data = urllib2.urlopen("http://api.rapgenius.com/songs/" + str(id))
    data = json.loads(json_data.read())
    return data

def get_song_lyrics(data):
    lyrics = []
    for i in data["response"]["song"]["lyrics"]["dom"]["children"][0]["children"]:
        if("children" not in i):
            if(json.dumps(i) != '{"tag": "br"}' and i != ' '):
                if(i[0] == ' '):
                    lyrics.append(i[1:])
                else:
                    lyrics.append(i)
        else:
            for x in i["children"]:
                if(json.dumps(x) != '{"tag": "br"}'):
                    lyrics.append(x)
    return lyrics

def get_prim_artist(data):
    return json.dumps(data["response"]["song"]["primary_artist"]["name"])[1:-1]

def get_feat_artist(data):
    farts= []
    for i in data["response"]["song"]["featured_artists"]:
        farts.append(json.dumps(i["name"])[1:-1])
    return farts


