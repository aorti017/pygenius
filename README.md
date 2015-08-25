ATTENTION
==========
Due to updates concerning the api utilized by this project, development and support have tentatively ceased. 

PyGenius
==========

Program Overview
----------
PyGenius is a library that can be used to access that data available at
http://rap.genius.com by utilizing their API.

Classes
---------
```
artist(artist id):
    - name(string)
    - description(string)
    - songs(array of strings)
song(song id):
    - name(string)
    - lyrics(array of strings)
    - primary_artist(string)
    - featured_artists(array of strings)
```

Functions
---------
```
search_song(query):
    - returns a song object for the result most like the query
```

Usage
----------
Example usage of the library can be found in ```./example.py```

Bugs/Limitations
---------
* Languages other than English are omitted and replaced by the
  language surrounded by ```{}```
* Due to annotations, line  are sometimes spliced.
* Currently the "songs" attibute of the artist class only contatins the title of the track and not the tracks id.
* The overall project is no longer functional because of updates to the Genius api.
