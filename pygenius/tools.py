def cat_lyrics(x):
	final = ""
	for i in x.lyrics:
		if(i[0] != ' ' and final != ""):
			final += ' '
		final += i
	return final
