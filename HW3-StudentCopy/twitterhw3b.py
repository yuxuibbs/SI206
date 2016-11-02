# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.


# code based on sentiments.py

import tweepy
from textblob import TextBlob

# copy/past twitter API stuff here


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

public_tweets = api.search('#speedcubing')

subjectivityTotal = 0
polarityTotal = 0

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)

print(type(analysis.sentiment))
# TODO: calculate average
print("Average subjectivity is")#, len(public_tweets) / subjectivityTotal)
print("Average polarity is")
