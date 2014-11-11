import json
import urllib2

class song:
    def __init__(self, id):
        json_data = urllib2.urlopen("http://api.rapgenius.com/songs/" + str(id))
        data = json.loads(json_data.read())
        self.lyrics = []
        for i in data["response"]["song"]["lyrics"]["dom"]["children"][0]["children"]:
            try:
                for x in range(0, len(i["children"]), 2):
                    self.lyrics.append(json.dumps(i["children"][x])[1:-1])
            except TypeError:
                tmp = ""
            except KeyError:
                tmp =""
        self.artist = json.dumps(data["response"]["song"]["primary_artist"]["name"])[1:-1]

#s = song(3893)
#for i in s.lyrics:
#    print i
#print s.artist
