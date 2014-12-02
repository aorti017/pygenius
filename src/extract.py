import urllib2
import json

#gets the json data for the corresponding song id
def get_song_data(id):
    json_data = urllib2.urlopen("http://api.rapgenius.com/songs/" + str(id))
    data = json.loads(json_data.read())
    return data
    
#gets the song title
def get_song_name(data):
    return data["response"]["song"]["title"]

#parses the data for the song's lyrics
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

#gets the primary artists
def get_prim_artist(data):
    return json.dumps(data["response"]["song"]["primary_artist"]["name"])[1:-1]

#parses the data for the featured artists
def get_feat_artist(data):
    farts= []
    for i in data["response"]["song"]["featured_artists"]:
        farts.append(json.dumps(i["name"])[1:-1])
    return farts

#gets the json data for the corresponding artist id
def get_artist_data(id):
    json_data = urllib2.urlopen("http://api.rapgenius.com/artists/" + str(id))
    data = json.loads(json_data.read())
    return data

#gets the artist's description if available
def get_artist_description(data):
    try:
        return data["response"]["artist"]["description"]["dom"]["children"][0]["children"][0]
    except KeyError:
        return ""

#gets the artist's name
def get_artist_name(data):
    return data["response"]["artist"]["name"]
