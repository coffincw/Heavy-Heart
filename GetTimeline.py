import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
from SentimentAnalyzer import TwitterClient

class TimelineGetter(object):
  def __init__(self, *args, **kwargs):
    consumer_key = 'n4zRm3xuVoYoBHDLbSSqCxlII'
    consumer_secret = 'i2bxYM53rVNv0NFnO4iALdUYUDXHSEp9JARjpSu6290B5W6BLj'
    access_token = '3265727682-sWioD71Vv1zJie1KCERyHZWgzCdDsGAy3lzdLJA'
    access_token_secret = 'Ir9vMlPyiJwafcqXOiRJgtdWpev2VU3rI0Z2MWXlJ79SV'

    # attempt authentication
    try:
      # create OAuthHandler object
      self.auth = OAuthHandler(consumer_key, consumer_secret)
      # set access token and secret
      self.auth.set_access_token(access_token, access_token_secret)
      # create tweepy API object to fetch tweets
      self.api = tweepy.API(self.auth)
    except:
      print("Error: Authentication Failed")
    return super().__init__(*args, **kwargs)

  def getTweets():
    tc = TwitterClient()
    tweets = tc.





