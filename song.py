import  extract
import json

class song:
    def __init__(self, id):
        data = extract.get_song_data(id)
        self.lyrics = extract.get_song_lyrics(data)
        self.artist = extract.get_prim_artist(data)

#s = song(3893)
#for i in s.lyrics:
#    print i
#print s.artist
