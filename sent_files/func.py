import os
import sys
sys.path.insert(0, '../config')
from twitter_config import api
import tweepy
import re
# encoding=utf8  
reload(sys)  
sys.setdefaultencoding('utf8')


def get_user_timeline_tweets(usernames):
	global api
	# grab recent timeline tweets by selected twitter user_names. Pass in as list.
	u_names = usernames
	for username in u_names:
		user = api.get_user(username)
		tweets = []
		tweet = api.user_timeline(user_id = user.id, count =20)
		for i in tweet:
			tweets.append(i.text)
	return tweets

def recent_tweets(search_word, num_find = 100):
	#grabs recent tweets by query. checks user of tweet removes users likley to be spam or bots.
	global api
	query = search_word
	max_tweets = num_find
	tweets = []
	count_added = 0
	count_removed = 0
	searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]
	for j in searched_tweets:
		followers = j.author.followers_count
		favorites = j.author.favourites_count
		statuses_count  = j.author.statuses_count
		background_img = j.author.profile_use_background_image
		screen_name = j.author.screen_name
		profile_img = j.author.default_profile_image
		tweet = j.text.encode('utf-8')
		retweeted = j.retweeted

		# print(j.retweeted)
		#print(followers, favorites, statuses_count, background_img, profile_img, screen_name)
		if followers > 20 and favorites > 20 and statuses_count > 20 and profile_img == False and remove_spamy_tweets(tweet) == 0 and retweeted == False:
			# if remove_spamy_tweets(tweet) == 0 and remove_retweets(tweet) == 0:
			# print(tweet)
			tweets.append(tweet)
			count_added += 1
		else:
			count_removed += 1
	print(count_added, count_removed)
	return (query,tweets)


def remove_spamy_tweets(tweet_string):
	# uses voting system to remove tweets that are spamy
	# when called check if return is 0 if not remove tweet.
	vote = 0
	tweet = str(tweet_string.lower())
	spammy_phrases = ["special offer", "money making", "make money", "start earning", "earn bitcoin"]
	for spammy_phrase in spammy_phrases:
		found = re.findall('\\b' + spammy_phrase + '\\b', tweet)
		if found:
		    vote += 1
	print('spammy tweets removed', vote)
	return vote




