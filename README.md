PyGenius
==========

Program Overview
----------
PyGenius is an API that can be used to access that data available at
http://rap.genius.com by utilizing their private API.

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
Usage
----------
Example usage of the API can be found in ```src/example.py```

Bugs/Limitations
---------
* Languages other than English are omitted and replaced by the
  language surrounded by ```{}```
* Due to annotations, line  are sometimes spliced.
* Currently the "songs" attibute of the artist class only contatins the title of the track and not the tracks id.
