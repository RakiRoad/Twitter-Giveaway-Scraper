#import libraries
import tweepy

#probably do not need this
import csv 

#Twitter API information
consumer_key = "gsD8iFLqvQDdg22OFAHIhcIx9"
consumer_secret = "AiNjNSFUXwFRcD5CxFhrNhTNhrBm7ggznhSBhUIiDeXpChw07h"
access_key = "867029806944309254-Au0d3L1PpESXyyVSjGrqWBUdPOJspIC"
access_secret = "KRV42V1w9gHBlI4gxMSMtCEVZIp8CFpIG3HmKYT88P7FF"

#Authentication Process
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#utilizes search to look for giveaways and retweets found results
def search_func(value):
	search_results = api.search(q=value, count=200)

	outtweets_id = [[result.id] for result in search_results]
	#outtweets_id = [search_results.id]
	length = len(outtweets_id)
	#print (outtweets_id)

	for i in range (0, length):
			api.retweet(outtweets_id[i][0])


"""
Major Issues:
	-Runs into errors when it tries to retweet duplicate tweets
		a conditional statement needs to be added to fix this

Features to be implemented:
	-We need to make the program keep searching for new giveaways so far only runs a single instance
	-Add functionality so program automatically retweets, follows, favorite tweet for giveaway
		-only does retweeet only so far

Twitter account information
	Email: redditfreebies28@gmail.com
	Password: Rockyisgod28
"""

#The Parameter it searches for 
search_func("giveaway retweet")