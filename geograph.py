
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
from collections import Counter
import ast

consumer_key = 'WRxcgZHq8HOA9AiACeoz7pc61'
consumer_secret = 'IJnOARqL3baljF5VfMPB4Gy1GmxVLlSv6L4BgJoh3bVDslSQYL'
access_token = '32554005-yIgL0lbl0aWXyJ0E8q61zDF8BpOtVzWwRoZyCDm1n'
access_token_secret = 'PzknR8jcAmNgG35G0D99BH9qEJfF7n477AxK1kgFDnVWl'

# Load credentials from json file
with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

# Instantiate an object
python_tweets = Twython(consumer_key, consumer_secret)

def process_tweet(tweet):
    d = {}
    d['hashtags'] = [hashtag['text'] for hashtag in tweet['entities']['hashtags']]
    d['text'] = tweet['text']
    d['user'] = tweet['user']['screen_name']
    d['user_loc'] = tweet['user']['location']
    return d


# Create a class that inherits TwythonStreamer
class MyStreamer(TwythonStreamer):

    # Received data
    def on_success(self, data):

        # Only collect tweets in English
        if data['lang'] == 'en':
            tweet_data = process_tweet(data)
            self.save_to_csv(tweet_data)

    # Problem with the API
    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()

    # Save each tweet to csv file
    def save_to_csv(self, tweet):
        with open(r'newsaved_tweets.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow(list(tweet.values()))


# Instantiate from our streaming class
stream = MyStreamer(consumer_key, consumer_secret,
                    access_token, access_token_secret)
# Start the stream
stream.statuses.filter(track='safaricom')


# tweets = pd.read_csv("newsaved_tweets.csv")
# tweets.head()
#
#
# print(tweets)
#
#
# # Extract hashtags and put them in a list
# list_hashtag_strings = [entry for entry in tweets.hashtags]
# list_hashtag_lists = ast.literal_eval(','.join(list_hashtag_strings))
# hashtag_list = [ht.lower() for list_ in list_hashtag_lists for ht in list_]
#
# # Count most common hashtags
# counter_hashtags = Counter(hashtag_list)
# counter_hashtags.most_common(20)
# print(counter_hashtags)
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
#
