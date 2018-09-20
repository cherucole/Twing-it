from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
import tweepy
from textblob import TextBlob
import json
import sys
import time
import re
import csv
import os
import time
from datetime import datetime
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from flask import Flask, render_template, url_for, jsonify, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField




consumer_key = 'WRxcgZHq8HOA9AiACeoz7pc61'
consumer_secret = 'IJnOARqL3baljF5VfMPB4Gy1GmxVLlSv6L4BgJoh3bVDslSQYL'

access_token = '32554005-yIgL0lbl0aWXyJ0E8q61zDF8BpOtVzWwRoZyCDm1n'
access_token_secret = 'PzknR8jcAmNgG35G0D99BH9qEJfF7n477AxK1kgFDnVWl'




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

    # Passes in a user id to this function and the function queries
    #  the database and gets a user's id as a response



f = open('search.csv', 'w+')
f.close()
f = open('datam.csv', 'w+')
f.close()



class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User {self.username}'


class Listener(StreamListener):
    counter = 0

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

        data = [user_name, tweet_time, polarity, subjectivity, tweet]

        print(data)
        print(self.counter)
        self.counter = self.counter + 1

        with open('search.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
            csvFile.close()

        # if int(datetime.utcnow().strftime('%s'))%10 == 0:
        reader = csv.reader(open('search.csv', 'r'))
        # reader1 = csv.reader(open('datam.csv', 'rb'))
        writer = csv.writer(open('datam.csv', 'w+'))
        for row in reader:
            writer.writerow(row)
        # now = 0
        if self.counter >= 50:
            print('im done')
            return False
        return True

    def on_error(self, status):
        print(str(status) + ' error found')

    @classmethod
    def runTweets(cls, topic):
        l = cls()
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, l)
        stream.filter(track=[topic])



