from pygenius import *

#Bambu's Golden Era Shower
#s = song.song(489522)

#Cool Calm Pete's 2 A.M.
#s = song.song(255949)

#Blue Scholar's Sagab
s = song(3893)

#prints the song title
print s.name

#prints the lyrics
for i in s.lyrics:
    print i

#prints primary artist
print s.primary_artist

#prints featured artists
for i in s.featured_artists:
    print i

#Bambu
#a = artist.artist(12246)

#Cool Calm Pete
#a = artist.artist(12283)

#Blue Scholars
a = artist(544)

#prints artist's name
print a.name

#prints artist's description if available
print a.description

#prints the artist's songs
for i in a.songs:
    print i
