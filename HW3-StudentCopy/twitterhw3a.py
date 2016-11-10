# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

# Name: Yuxuan Chen

import tweepy
import os

# twitter access stuff


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

# path for image
img = os.path.abspath('cubingclub.png')

# post image
api.update_with_media(img, status="Michigan Cubing Club logo #UMSI-206 #Proj3")