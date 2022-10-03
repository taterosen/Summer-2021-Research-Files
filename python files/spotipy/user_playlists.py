#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 11:56:52 2021

@author: taterosen

show playlists
"""

# Shows a user's playlists (need to be authenticated via oauth)

import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipyCred
'''
if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Whoops, need a username!")
    print("usage: python user_playlists.py [username]")
    sys.exit()
'''
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotipyCred.client_id, client_secret= spotipyCred.client_secret, redirect_uri=spotipyCred.redirect_url))

playlists = sp.user_playlists('0tatertot0')

for playlist in playlists['items']:
    print(playlist['name'])