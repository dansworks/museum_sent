import os
import sys

sys.path.insert(0, '../config')
from twitter_config import api
import tweepy



def get_user_timeline_tweets(usernames):
	global api
	u_names = usernames
	for username in u_names:
		user = api.get_user(username)
		tweets = []
		# print(user.screen_name)
		# print(user.id)
		tweet = api.user_timeline(user_id = user.id, count =20)

		# tweet_status = api.statuses_lookup()
		for i in tweet:
			# print(i.text)
			tweets.append(i.text)

	print(len(tweets))	

	return tweets

def recent_tweets(search_word, num_find = 100):
	global api
	query = search_word
	max_tweets = num_find
	tweets = []
	searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]
	for j in searched_tweets:
		print(j.text)
		tweets.append(j.text)


	return (query,tweets)