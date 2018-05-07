import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

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

displayName = user['display_name']
followers = user['followers']['total']

while True:
	print()
	print('>>> Welcome to Spotipy ' + displayName + '!')
	print('>>> You have ' + str(followers) + ' followers.')
	print()
	print('0 - Search for an artist')
	print('1 - exit')
	print()
	choice = input('Your choice: ')

# Search for the artist
	if choice == '0':
		print(spotipyObject.me( ))
		print()
		searchQuery = input("0k, what's their name?: ")
		print()
		# Get search results
		searchResults = spotipyObject.search(searchQuery,1,0,'artist')
		# print(json.dumps(searchResults, sort_keys=True,indent=4))

		# artist details

		artist = searchResults['artists']['items'][0]
		print(artist['name'])
		print(str(artist['followers']['total']) + 'followers')
		print(artist['genres'])
		print()
		webbrowser.open(artist['images'][0]['url'])
		artistID = artist['id']

		# album and track details
		trackURIs = []
		trackArt = []
		z = 0

		# Extract album data
		albumResults = spotipyObject.artist_albums(artistID)
		albumResults = albumResults['items']
		# print(current_user_playing_track)

		for item in albumResults:
			# looping through album
			print('ALBUM ' + item['name'])
			albumID = item['id']
			albumArt = item['images'][0]['url']

			# Extract track data
			trackResults = spotipyObject.album_tracks(albumID)
			trackResults = trackResults['items']


			for item in trackResults:
				# looping through track results
				print(str(z) + ':' + item['name'])
				trackURIs.append(item['uri'])
				trackArt.append(albumArt)
				z += 1
			print()

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







