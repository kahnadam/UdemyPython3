#notes on data structure:
#the playlist overall is a dictionary
playlist = {
	"title": "python jams",
	"author": "adam kahn",
#the songs value is a list, and the items of the list are each dictionaries (one for each song)
#some songs have multiple artists on them, in a list
	"songs": [
		{"title": "A Day in the Life", "artist": ["The Beatles"], "duration": 5.2},
		{"title": "Dream On", "artist": ["Aerosmith", "GRiZ"], "duration": 5.0},
		{"title": "Killer Queen", "artist": ["Queen"], "duration": 3.0 }
	]
}

#what songs are in the playlist?
for song in playlist["songs"]:
	print(song["title"])

#how long is the playlist?
total_length = 0
for song in playlist["songs"]:
	total_length += song["duration"]
print(total_length)