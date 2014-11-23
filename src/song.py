import extract
import json

class song:
    def __init__(self, id):
        data = extract.get_song_data(id)
        self.lyrics = extract.get_song_lyrics(data)
        self.primary_artist = extract.get_prim_artist(data)
        self.featured_artists = extract.get_feat__artist(data)
