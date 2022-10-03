#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 28 10:43:24 2021

@author: taterosen
"""

from googleapiclient.discovery import build

api_key = "AIzaSyDEI1p0-Jvg-4i0F7_40fxr0uE1ilJKeaY"

youtube = build('youtube', 'v3', developerKey= api_key)

request = youtube.channels().list(
        part='statistics',
        forUsername='schafer5'
    )

response = request.execute()

print(response)