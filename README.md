PyGenius
==========

Program Overview
----------
PyGenius is an API that can be used to access that data available at
http://rapgenius.com by utilizing their private API.

Classes
---------
```
artist(artist id):
    - name(string)
    - description(string)

song(song id):
    - name (string)
    - lyrics(array of strings)
    - primary_artist(string)
    - featured_artists(array of strings)
```

Bugs/Limitations
---------
* Languages other than English are omitted and replaced by the
  language surrounded by ```{}```
* Due to annotations, line  are sometimes spliced.
