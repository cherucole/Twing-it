from __future__ import unicode_literals
import tweepy #The Twitter API
from time import sleep
from datetime import datetime
from textblob import TextBlob #For Sentiment Analysis
import matplotlib.pyplot as plt #For Graphing the Data
import psycopg2
import sys
from twython import Twython
import json
import pandas as pd

consumer_key = 'WRxcgZHq8HOA9AiACeoz7pc61'
consumer_secret = 'IJnOARqL3baljF5VfMPB4Gy1GmxVLlSv6L4BgJoh3bVDslSQYL'
access_token = '32554005-yIgL0lbl0aWXyJ0E8q61zDF8BpOtVzWwRoZyCDm1n'
access_token_secret = 'PzknR8jcAmNgG35G0D99BH9qEJfF7n477AxK1kgFDnVWl'

# Load credentials from json file
with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

# Instantiate an object
python_tweets = Twython(consumer_key, consumer_secret)

# Create our query
query = {'q': 'safaricom',
        'result_type': 'recent',
        'count': 300,
        'lang': 'en',
        }

# Search tweets
dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': [], 'polarity':[], 'subjectivity': []}
non_bmp_map= dict.fromkeys(range(0x10000, sys.maxunicode +1), 0xfffd)


for tweet in python_tweets.search(**query)['statuses']:

    print(tweet['text'].translate(non_bmp_map))

    analysis = TextBlob(tweet['text'].translate(non_bmp_map))

    print(analysis.sentiment)
    print("")

    dict_['user'].append(tweet['user']['screen_name'])
    dict_['date'].append(tweet['created_at'])
    dict_['text'].append(tweet['text'])
    dict_['favorite_count'].append(tweet['favorite_count'])
    dict_['polarity'].append(analysis.sentiment.polarity)
    dict_['subjectivity'].append(analysis.sentiment.subjectivity)

    print(tweet)

# Structure data in a pandas DataFrame for easier manipulation
df = pd.DataFrame(dict_)
df.sort_values(by='favorite_count', inplace=True, ascending=False)
df.head(200)
df.to_csv('redsan1.csv')

print(df)



# Store it ina csv
# Load credentials from json file
