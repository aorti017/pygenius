import  song
import artist

#Bambu's Golden Era Shower
#s = song.song(489522)

#Blue Scholar's Sagab
#s = song.song(3893)

#Cool Calm Pete's 2 A.M.
s = song.song(255949)

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

#Blue Scholars
#a = artist.artist(544)

#Cool Calm Pete
a = artist.artist(12283)
print a.name
print a.description
