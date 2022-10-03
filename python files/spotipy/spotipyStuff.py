#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:33:45 2021

@author: taterosen
"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import spotipyCred
import sys

scope = "user-read-recently-played"
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotipyCred.client_id, client_secret= spotipyCred.client_secret, redirect_uri=spotipyCred.redirect_url, scope=scope))
"""
results = sp.current_user_recently_played()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])

"""
"""
### list the names of all the albums released by the artist Harry Styles
harry_uri = 'spotify:artist:6KImCVD70vtIoJWnq6nGn3'
#spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.artist_albums(harry_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
"""
"""
### get 30 second samples and cover art for the top 10 tracks for Led Zeppelin
lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

#spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()
"""
"""
###get the URL for an artist image given the artist’s name
if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = 'Radiohead'

results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]
    print(artist['name'], artist['images'][0]['url'])
"""



