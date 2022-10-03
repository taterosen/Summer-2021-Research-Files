#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 14:25:16 2021

@author: taterosen
"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time
import spotipyCred

cid = spotipyCred.client_id
cs = spotipyCred.client_secret

ccm = SpotifyClientCredentials(client_id=cid, client_secret=cs)
sp = spotipy.Spotify(client_credentials_manager=ccm)

def getTrackIDs(user, pid):
    ids = []
    playlist = sp.user_playlist(user, pid)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return ids

ids = getTrackIDs('Username', '4RJsISf4h72ZiwUZEWoC5j')


def getTrackFeatures(id):
    meta = sp.track(id)
    features = sp.audio_features(id)
    
    # meta
    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    release_date = meta['album']['release_date']
    length = meta['duration_ms']
    popularity = meta['popularity']
    
    # features
    acousticness = features[0]['acousticness']
    danceability = features[0]['danceability']
    energy = features[0]['energy']
    instrumentalness = features[0]['instrumentalness']
    liveness = features[0]['liveness']
    loudness = features[0]['loudness']
    speechiness = features[0]['speechiness']
    tempo = features[0]['tempo']
    time_signature = features[0]['time_signature']
    
    track = [name, album, artist, release_date, length, popularity, acousticness,
              danceability, energy, instrumentalness, liveness, loudness,
              speechiness, tempo, time_signature]
    return track

print(len(ids))
print(ids)


# loop over track ids
tracks = []
for i in range(len(ids)):
    time.sleep(.5)
    track = getTrackFeatures(ids[i])
    tracks.append(track)
    
# create dataset
data = pd.DataFrame(tracks, columns = ['name', 'album', 'artist', 'releas_date',
                                       'length', 'popularity', 'acousticness',
                                       'danceability', 'energy', 'instrumentalness',
                                       'liveness', 'loudness', 'speechiness',
                                       'tempo', 'time_signature'])
data.to_csv("playlist.csv", sep = ',')






