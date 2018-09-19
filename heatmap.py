from __future__ import unicode_literals
import tweepy #The Twitter API
from time import sleep
from datetime import datetime
from textblob import TextBlob #For Sentiment Analysis
import matplotlib.pyplot as plt #For Graphing the Data
import psycopg2
import sys
from twython import Twython, TwythonStreamer
import json
import pandas as pd
from geopy.geocoders import Nominatim
import gmplot
import csv

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
query = {'q': 'Senate',
        'result_type': 'recent',
        'count': 1000,
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
df.head(1000)
df.to_csv('senate.csv')

print(df)


#
#
#
# geolocator = Nominatim()
#
# # Go through all tweets and add locations to 'coordinates' dictionary
# coordinates = {'latitude': [], 'longitude': []}
# for count, user_loc in enumerate(tweets.location):
#     try:
#         location = geolocator.geocode(user_loc)
#
#         # If coordinates are found for location
#         if location:
#             coordinates['latitude'].append(location.latitude)
#             coordinates['longitude'].append(location.longitude)
#
#     # If too many connection requests
#     except:
#         pass
#
# # Instantiate and center a GoogleMapPlotter object to show our map
# gmap = gmplot.GoogleMapPlotter(30, 0, 3)
#
# # Insert points on the map passing a list of latitudes and longitudes
# gmap.heatmap(coordinates['latitude'], coordinates['longitude'], radius=20)
#
# # Save the map to html file
# gmap.draw("python_heatmap.html")
#
# # Store it ina csv
# # Load credentials from json file
#
#
#
#

# Filter out unwanted data
# def process_tweet(tweet):
#     d = {}
#     d['hashtags'] = [hashtag['text'] for hashtag in tweet['entities']['hashtags']]
#     d['text'] = tweet['text']
#     d['user'] = tweet['user']['screen_name']
#     d['user_loc'] = tweet['user']['location']
#     return d
#
#
# # Create a class that inherits TwythonStreamer
# class MyStreamer(TwythonStreamer):
#
#     # Received data
#     def on_success(self, data):
#
#         # Only collect tweets in English
#         if data['lang'] == 'en':
#             tweet_data = process_tweet(data)
#             self.save_to_csv(tweet_data)
#
#     # Problem with the API
#     def on_error(self, status_code, data):
#         print(status_code, data)
#         self.disconnect()
#
#     # Save each tweet to csv file
#     def save_to_csv(self, tweet):
#         with open(r'saved_tweets.csv', 'a') as file:
#             writer = csv.writer(file)
#             writer.writerow(list(tweet.values()))
#
#
# # Instantiate from our streaming class
# stream = MyStreamer(consumer_key, consumer_secret,
#                     access_token, access_token_secret)
# # Start the stream
# stream.statuses.filter(track='python')
#
#
# tweets = pd.read_csv("saved_tweets.csv")
# tweets.head()