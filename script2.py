# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 17:21:46 2019

@author: Parth
"""
import time
import threading
import urllib
import re
import io
import active
import re
import sys
from time import sleep
import pickle
import os
from textblob import TextBlob
from math import ceil
from pathlib import Path
import pandas as pd
import concurrent.futures 
import psycopg2
import GetOldTweets3 as got
import tweepy

table= "keywords"
count=0

query="SELECT distinct id, name, username, tweet_text, created_at, location, polarity FROM public.keywords"

try:     
    conn = psycopg2.connect(database='Hiranandani', user = "postgres", password = "parth123n@#*", host = "127.0.0.1", port = "5432")    
except:
    print("Create database first")


df=pd.read_sql(query,conn)



mycursor = conn.cursor()


for j,i in df.iterrows():
    sql = "INSERT INTO {} (id, name, username, tweet_text, created_at, location, polarity) VALUES \
        (%s, %s, %s, %s, %s, %s, %s)".format(table)
    val = (i['id'], i['name'],i['username'],i['tweet_text'], i['created_at'], i['location'],i['polarity'])
    mycursor.execute(sql, val)
    conn.commit()


conn.close()


