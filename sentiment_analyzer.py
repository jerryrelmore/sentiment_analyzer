#!/bin/python3

# File: sentiment_analysis_2.py
# Inspired by: https://www.dataquest.io/blog/streaming-data-python/

import sys
import tweepy
import json
from textblob import TextBlob
import MySQLdb
from sqlalchemy.exc import ProgrammingError
import dataset
import auth_keys
import settings

# Set auth and connect to Twitter using Tweepy 

auth = tweepy.OAuthHandler(auth_keys.OAUTH_CONSUMER_KEY, auth_keys.CONSUMER_API_SECRET_KEY)
auth.set_access_token(auth_keys.OAUTH_TOKEN, auth_keys.OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

# Connect to our MariaDB database (tweet_sentiment_analysis)
try:
    # utf8mb4 encoding is necessary because Twitter uses 4 byte characters for things like emojis
    db = dataset.connect(settings.CONNECTION_STRING)
    print("Database connection successful!")
except:
    print("Database connection failed\n")
    print("Unexpected error:", sys.exc_info()[0])
    raise

class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        
        # Pull some additional data from the streaming tweets
        description = status.user.description
        loc = status.user.location
        coords = status.coordinates
        geo = status.geo
        name = status.user.screen_name
        user_created = status.user.created_at
        followers = status.user.followers_count
        id_str = status.id_str
        created = status.created_at
        retweets = status.retweet_count
        bg_color = status.user.profile_background_color

        # Convert coordinates JSON dictionary to string (if coordinates are available)
        if geo is not None:
            geo = json.dumps(geo)
        
        if coords is not None:
            coords = json.dumps(coords)

        # Below two lines filter out retweets - if we want retweets, comment if...and return... out.
        try:
            if status.retweeted_status:
                return
        except AttributeError:
            # If we want to write to file (rather than/in addition to database), uncomment and set file name below
            #with open("twitter-stock-stream.json", "w") as f:
            #    f.write(str(status))
            # If the tweet is long (>140 chars) it will come back in an extended_tweet dict. Print the full text of that tweet rather than truncated.
            try:
                if status.extended_tweet['full_text']:
                    text = status.extended_tweet['full_text']
                    print(text)
            except AttributeError:
                # If tweet <=140 chars go ahead and print standard text return
                text = status.text
                print(text)
        
        # Let's do some sentiment analysis with TextBlob
        blob = TextBlob(text)
        sentimentience = blob.sentiment

        # Extract polarity and subjectivity from the tweet.
        # Polarity: negativity or positivity of the tweet on a -1 to 1 scale
        # Subjectivity: how objective or subjective the tweet is on a 0 (very objective) to 1 (very subjective) scale
        polarity = sentimentience.polarity
        subjectivity = sentimentience.subjectivity

        # Write tweets to the database
        try:
            table = db[settings.TABLE_NAME]
            table.insert(dict(
                user_description=description,
                user_location=loc,
                coordinates=coords,
                text=text,
                user_name=name,
                user_created=user_created,
                user_followers=followers,
                id_str=id_str,
                created=created,
                retweet_count=retweets,
                user_bg_color=bg_color,
                polarity=sentimentience.polarity,
                subjectivity=sentimentience.subjectivity,
            ))
        except ProgrammingError as err:
            print(err)

    def on_error(self, status_code):
        if status_code == 420:
            return False

stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener, tweet_mode='extended')
stream.filter(track=settings.TRACK_TERMS)

