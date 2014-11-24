import extract

class artist:
    def __init__(self, id):
        data = extract.get_artist_data(id)
        self.name = extract.get_artist_name(data)
        self.description = extract.get_artist_description(data)
        #to be added along with search
        #self.top_tracks = extract.get_artist_tracks(data)
