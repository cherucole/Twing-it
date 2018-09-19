import tweepy
from textblob import TextBlob
import json
import sys
import time
import re
import csv

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


consumer_key = 'WRxcgZHq8HOA9AiACeoz7pc61'
consumer_secret = 'IJnOARqL3baljF5VfMPB4Gy1GmxVLlSv6L4BgJoh3bVDslSQYL'

access_token = '32554005-yIgL0lbl0aWXyJ0E8q61zDF8BpOtVzWwRoZyCDm1n'
access_token_secret = 'PzknR8jcAmNgG35G0D99BH9qEJfF7n477AxK1kgFDnVWl'

class Listener(StreamListener):
    def on_data(self, data):
        row = []
        all_data = json.loads(data)
        user_name = " ".join(re.findall('[a-zA-Z]+', all_data['user']['name']))
        row.append(user_name)
        tweet_time = " ".join(re.findall('[a-zA-Z]+', all_data["created_at"]))
        row.append(tweet_time)
        tweet = " ".join(re.findall('[a-zA-Z]+', all_data['text']))
        row.append(tweet)
        blob = TextBlob(tweet)
        polarity = blob.sentiment.polarity
        row.append(polarity)
        subjectivity = blob.sentiment.subjectivity
        row.append(subjectivity)

        print (row)
        data = f'{user_name}, {tweet_time}, {polarity}, {subjectivity}, {tweet}'

        with open('datauhuru.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)

        csvFile.close()
        return True

    def on_error(self, status):
        print (str(status) + ' error found')


l = Listener()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track=['Senate'])

