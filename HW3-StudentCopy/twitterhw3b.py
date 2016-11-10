# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

# Name: Yuxuan Chen
# code based on sentiments.py

import tweepy
from textblob import TextBlob

# insert twitterAPI codes here


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

public_tweets = api.search('#speedcubing')

# sum of subjectivity and polarities
subjectivityTotal = 0
polarityTotal = 0

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    subjectivityTotal += analysis.sentiment.subjectivity
    polarityTotal += analysis.sentiment.polarity
    print()

# calculate average subjectivity and polarity
print("Average subjectivity is", subjectivityTotal / len(public_tweets))
print("Average polarity is", polarityTotal / len(public_tweets))
