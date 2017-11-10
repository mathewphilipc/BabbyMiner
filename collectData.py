import tweepy
from tweepy import OAuthHandler
import sys
sys.path.insert(0,'/home/mathew')
import twitter_secret

consumer_key = '6SSlw3YCpX0kgT7U3rPKixC1M'
consumer_secret = twitter_secret.consumer_secret
access_token = twitter_secret.access_token
access_secret = twitter_secret.access_secret
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

# print("hello world")
#print(consumer_secret)
for status in tweepy.Cursor(api.home_timeline).items(20):
    # Process a single status
    print("New tweet:\n\n" + status.text + "\n\n")