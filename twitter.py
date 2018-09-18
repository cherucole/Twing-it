import tweepy #The Twitter API
from time import sleep
from datetime import datetime
from textblob import TextBlob #For Sentiment Analysis
import matplotlib.pyplot as plt #For Graphing the Data
import psycopg2
import json



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)

#
# searchTerm = input("Enter keyword/hastag to search about")
# print(searchTerm)
# no_searches = int(input("Enter number of tweets to analyze"))
# print(no_searches)
# longitude = float(input('Enter Longitude values here').strip())
# latitude = float(input('Enter Latitude values here').strip())
# radius = int(input('Enter radius values in km here').strip())
#
# geo=f"{longitude},{latitude},{radius}km"
#
# print(geo)
# print(type(geo))
#
# tweets = tweepy.Cursor(api.search, q=searchTerm, lang="English").items(no_searches)
#
# for tweet in tweepy.Cursor(api.search,q=searchTerm, geocode=geo).items(100):
#    print ([tweet.created_at, tweet.text.encode('utf-8'), tweet.user.id, tweet.geo])


##    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'), tweet.user.id])
##
##positive = 0
##negative = 0
##neutral = 0
##polarity = 0
##'-33.602131,-70.576876,100000km'
##for tweet in tweets:
##    print(tweet)



# Using the API object to get tweets from your timeline, and storing it in a variable called public_tweets



# The search term you want to find
query = "#ISupportUhuruCuts"
# Language code (follows ISO 639-1 standards)
language = "en"
rpp=10
geocode = "0.0236,37.9062,1000km"

# Calling the user_timeline function with our parameters
results = api.search(q=query, lang=language, geocode=geocode, rpp=rpp)

# foreach through all tweets pulled
# for tweet in results:
#    # printing the text stored inside the tweet object
#    # print (tweet.user.screen_name,"Tweeted:",tweet.text)
#  # add to JSON
#     with open('tweets.json', 'w', encoding='utf8') as file:
#       json.dump(tweet._json, file)
#

for tweet in results:

        # add to JSON

   with open('tweets.json', 'w', encoding='utf8') as file:
    json.dump(tweet._json, file)
   print(tweet)

#
# # Postgresql initialization
# connection = psycopg2.connect("dbname=twing user=melissamalala")
# cursor = connection.cursor()
#
# # The table schema: CREATE TABLE tweets (id SERIAL PRIMARY KEY, tweet_id BIGINT NOT NULL, text VARCHAR NOT NULL, screen_name VARCHAR NOT NULL, author_id INTEGER, created_at VARCHAR NOT NULL, inserted_at TIMESTAMP NOT NULL)
#
# try:
#     statuses = api.list_timeline(api.me().screen_name, '<NAME OF TIMELINE?>')
#     for s in statuses:
#         # To remove duplicate entries
#         # See http://initd.org/psycopg/docs/faq.html for "not all arguments converted during string formatting"
#         cursor.execute("SELECT id FROM tweets WHERE text = %s;", [s.text])
#         if cursor.rowcount == 0:
#             cursor.execute("INSERT INTO tweets (tweet_id, text, screen_name, author_id, created_at, inserted_at) VALUES (%s, %s, %s, %s, %s, current_timestamp);", (s.id, s.text, s.author.screen_name, s.author.id, s.created_at))
#             connection.commit()
# except tweepy.error.TweepError:
#     print "Whoops, could not fetch news!"
# except UnicodeEncodeError:
#     pass
# finally:
#     cursor.close()
#     connection.close()
#
#
#
