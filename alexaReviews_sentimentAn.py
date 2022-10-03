#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 11:43:08 2021

@author: taterosen

amazon alexa reviews sentiment analysis
"""

import pandas as pd

#load alexa reviews data
col_names = ["rating","date","variation","verified_reviews","feedback"]
df = pd.read_csv('amazon_alexa.tsv', names=col_names)

from textblob import TextBlob

for index, row in df.iterrows():
    review = row["verified_reviews"]
    text = TextBlob(review)
    
    #sentiment analysis
    subjectivity = text.sentiment.subjectivity  #runs from 0 to 1
    polarity = text.sentiment.polarity          #runs from -1 to 1
    print(review, subjectivity, polarity)
