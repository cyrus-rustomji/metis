import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
from collections import OrderedDict
import pickle
from collections import Counter

# Get username from terminal
username = sys.argv[1]

# User Id: 123181425

# Erase cache and prompt for user permission
try:
	token = util.prompt_for_user_token(username)
except:
	os.remove(f".cache-{username}")
	token = util.prompt_for_user_token(username)

# Create our spotipyObject
spotipyObject = spotipy.Spotify(auth=token)

user = spotipyObject.current_user()
# print(user)

displayName = user['display_name']
followers = user['followers']['total']
print()
print()
recommendation = spotipyObject.recommendation_genre_seeds()
print(recommendation)
print()
print()
i = 0
# rec = spotipyObject.recommendations(seed_artists='2YZyLoL8N0Wb9xBt1NhZWg')
# print(rec)

while True:
	print()
	print('>>> Welcome to Spotipy ' + displayName + '!')
	print('>>> You have ' + str(followers) + ' followers.')
	print()
	print('0 - Search for an artist')
	print('1 - exit')
	print()
	choice = input('Your choice: ')
	d = {}

# Search for the artist
	if choice == '0':
		# print(spotipyObject.me( ))
		print()
		searchQuery = input("Aight, what's their name?: ")
		print()
		# Get search results
		searchResults = spotipyObject.search(searchQuery,1,0,'artist')
		print(json.dumps(searchResults, sort_keys=True,indent=4))

		# artist details

		artist = searchResults['artists']['items'][0]
		name_of_artist = artist['name']
		popularity = artist['popularity']
		followers = str(artist['followers']['total']) 
		genres = artist['genres']
		print(popularity)
		print(name_of_artist)
		print(followers)
		print(genres)
		print()
		# commented out line below shows artists picture
		# webbrowser.open(artist['images'][0]['url'])
		artistID = artist['id']

		# album and track details
		trackURIs = []
		trackArt = []
		z = 0

		# Extract album data
		albumResults = spotipyObject.artist_albums(artistID)
		albumResults = albumResults['items']
		# print(current_user_playing_track)
		albums = []

		for item in albumResults:
			# looping through album
			no_repeat_albums = item['name']
			albums.append(no_repeat_albums)
			# print('ALBUM ' + item['name'])
			albumID = item['id']
			# print(albums)
			# albumArt = item['images'][0]['url']

			# Extract track data
			trackResults = spotipyObject.album_tracks(albumID)
			trackResults = trackResults['items']


			# for item in trackResults:
			# 	# looping through track results
			# 	print(str(z) + ':' + item['name'])
			# 	trackURIs.append(item['uri'])
			# 	trackArt.append(albumArt)
				# z += 1
			albums2 = set(albums)

		d['artist'] = name_of_artist
		d['spotify_artist_id'] = artistID
		d['popularity'] = popularity
		d['followers'] = followers
		d['genres'] = genres
		d['count_of_genres'] = Counter(genres)
		d['total_of_genres'] = len(genres)
		d['albums'] = albums2
		print(d)
		# with open('wayne.pkl', 'wb') as handle:
		# 	pickle.dump(d, handle, protocol=pickle.HIGHEST_PROTOCOL)
		# see album art
		while True:
			songSelection = input('Enter a song number to see the album art associated with it (or set x to exit): ')
			if songSelection == 'x':
				break
			webbrowser.open(trackArt[int(songSelection)])


# End the program
	if choice == '1':
		break



# print(json.dumps(VARIABLE, sort_keys=True,indent=4))







