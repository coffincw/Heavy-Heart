import re
import tweepy
import SentimentAnalyzer
from tweepy import OAuthHandler
from textblob import TextBlob

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

def getTraining():
  tweets = SentimentAnalyzer.main("#depressed")
  anxiety = SentimentAnalyzer.main("#anxiety")
  tweets.extend([x for x in anxiety if x not in tweets])
  training = []
  for x in tweets:
    training.append(list(x.values())[0])

  for x in training:
    print(x)

if __name__ == "__main__":
    getTraining()










