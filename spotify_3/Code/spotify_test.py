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
# print(user)
print(json.dumps(spotipyObject, sort_keys=True,indent=4))
displayName = user['display_name']
followers = user['followers']['total']
print()
print()
recommendation = spotipyObject.recommendation_genre_seeds()
print(recommendation)
print()
print()
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

# Search for the artist
	if choice == '0':
		print(spotipyObject.me( ))
		print()
		searchQuery = input("0k, what's their name?: ")
		print()
		# Get search results
		searchResults = spotipyObject.search(searchQuery,1,0,'artist')
		print(json.dumps(searchResults, sort_keys=True,indent=4))

	if choice == '1':
		break


