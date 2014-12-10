import extract

class artist:
    def __init__(self, id):
        data, song_data  = extract.get_artist_data(id)
        self.name = extract.get_artist_name(data)
        self.description = extract.get_artist_description(data)
        self.songs = extract.get_artist_songs(song_data)
