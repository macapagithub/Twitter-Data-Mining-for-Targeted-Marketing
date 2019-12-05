# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 17:31:29 2019

@author: Parth
"""

import collections
from collections import Counter
import pickle 
import string
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from math import ceil
import tweepy
import active

#creating a separate folder for  each tweet
query='ShameOnAnjana'
profile_file=query+'/Profiles.csv'
status_file=query+'/status.csv'
tweets_file=query+'/tweets.pickle'

#Opening the file containing previously stored tweets
try:
    h=open(tweets_file,'rb')
except:
    print("Run the initial code first.")
stored_tweets=pickle.load(h)


#Extracting url data from previously stored tweets
tweets_id=active.get_tweet_id(stored_tweets)
url_list, username_list,user_profile_list=active.get_url_data(stored_tweets)

#Pulling new tweets and extending them with the stored tweets
searched_tweets=active.pull_tweets(query)
stored_tweets.extend(searched_tweets)
active.write_data(stored_tweets,tweets_file)


#Extracting url data from new stored tweets
url_list1, username_list1,user_profile_list1=active.get_url_data(searched_tweets)
user_profile_list.extend(user_profile_list1)



#Reading the file containing previously stored profile URLs
df=pd.read_csv(profile_file)
urls=list(df['Profile'])

#Only extend/add new profile URL if they are already not present
for i in user_profile_list:
    if i not in urls:
        urls.extend(i)
        
#Storing unique profile URLs in a file
urls1=set(urls)
urls_final=list(urls1)
d={'Profile':pd.Series(urls_final)}
finaldata=pd.DataFrame(d)
finaldata.to_csv(profile_file,index=False,encoding='UTF-8')

#Ensuring that only unique posts urls are stored
url_list.extend(url_list1)
url_set=set(url_list)
url_list_final=list(url_set)
df={'Posts URL':pd.Series(url_list_final)}
finaldata=pd.DataFrame(df)
finaldata.to_csv(status_file,index=False,encoding='UTF-8')

#Gives the frequency of profile's posts
counter=collections.Counter(urls_final)


#Analysis of negative tweets
neg=active.analytics(searched_tweets)
word=active.wordcloud(neg)




