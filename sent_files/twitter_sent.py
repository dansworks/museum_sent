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
# encoding=utf8  
reload(sys)  
sys.setdefaultencoding('utf8')

query_words = ["@sfmoma","elmuseo", "@oaklandmuseumca", "@asianartmuseum", "@MuseumModernArt", "@LACMA"]	


for q_word in query_words:
	try:
		q_word = recent_tweets(q_word, 500)
	except Exception as e:
		print(str(e))
	count = 0
	gross_subjectivity = 0
	gross_polarity = 0
	try:
		for tweet in q_word[1]: 
			blob = TextBlob(tweet)
			for sentence in blob.sentences:
				# print(sentence.sentiment)
				gross_polarity += sentence.sentiment.polarity
				gross_subjectivity +=sentence.sentiment.subjectivity
				count += 1
		avg_gp = gross_polarity/count * 100	
		avg_gs = gross_subjectivity/count * 100

		print([count, q_word[0]])
		print([avg_gp, avg_gs ])
		time.sleep(10)
	except Exception as e:
		print(str(e))

	try:
		# enter results into desired DB.
		print("---")
		# db_insert_recent_tweets_sent(avg_gp, avg_gs,'recent_tweets', q_word[0])
	except Exception as e:
		print(str(e))
	



