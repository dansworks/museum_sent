import os
import sys
sys.path.insert(0, '../config')
from textblob import TextBlob
from twitter_config import api
from db_con import cnx
import time
import mysql.connector
import tweepy
from tweepy import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import json


# # # # TWITTER STREAMER # # # #
class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """
    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
		listener = StdOutListener(fetched_tweets_filename)
		auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)
		stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords: 
		stream.filter(track=hash_tag_list)


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            data = json.loads(data)
            print(data["text"].encode('utf-8'))
            # time.sleep(2)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data["text"].encode('utf-8'))
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
          

    def on_error(self, status):
        print(status)

 
if __name__ == '__main__':
 
    # Authenticate using config.py and connect to Twitter Streaming API.
	hash_tag_list = ["Museum of Modern Art"]
	fetched_tweets_filename = "tweets.txt"

	twitter_streamer = TwitterStreamer()
	twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)

	


