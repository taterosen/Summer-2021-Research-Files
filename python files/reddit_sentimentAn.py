#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:26:14 2021

@author: taterosen

reddit vaccine myth sentiment analysis
"""

import pandas as pd

#load data downloaded from twitter
col_names = ["title","score","id","url","comms_numm","created","body","timestamp"]
df = pd.read_csv('reddit.csv', index_col=0, names=col_names)

from textblob import TextBlob

for index, row in df.iterrows():
    comment = row["body"]
    text = TextBlob(comment)
    
    #sentiment analysis
    subjectivity = text.sentiment.subjectivity  #runs from 0 to 1
    polarity = text.sentiment.polarity          #runs from -1 to 1
    print(comment, subjectivity, polarity)
