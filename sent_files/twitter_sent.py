import os
import sys

sys.path.insert(0, '../config')
from textblob import TextBlob

from twitter_config import api

from db_funcs import db_insert_recent_tweets_sent
from func import recent_tweets

import time

import mysql.connector
import tweepy


		
# museums = ['@legionofhonor', '@sfmoma', '@oaklandmuseumca', '@asianartmuseum', '@deyoungmuseum', '@sfmexicanmuseum']
museums = ['@legionofhonor', '@sfmoma', '@oaklandmuseumca', '@asianartmuseum', '@deyoungmuseum', '@MuseumModernArt', '@LACMA']



for museum in museums:
	try:
		tweet_arr = recent_tweets(museum, 100)
	except Exception as e:
		print(str(e))
	count = 0
	gross_subjectivity = 0
	gross_polarity = 0
	try:
		for tweet in tweet_arr[1]: 
			blob = TextBlob(tweet)

			for sentence in blob.sentences:
				print(sentence.sentiment)
				gross_polarity += sentence.sentiment.polarity
				gross_subjectivity +=sentence.sentiment.subjectivity
				count += 1

		avg_gp = gross_polarity/count * 100	
		avg_gs = gross_subjectivity/count * 100

		print([count, museum])
		print([avg_gp, avg_gs ])
		time.sleep(10)
	except Exception as e:
		print(str(e))

	try:
		db_insert_recent_tweets_sent(avg_gp, avg_gs,'recent_tweets', tweet_arr[0])
	except Exception as e:
		print(str(e))
	



