import re
import tweepy
import SentimentAnalyzer
from tweepy import OAuthHandler
from textblob import TextBlob

class GetTimeline(object):
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

  @staticmethod
  def getTraining():
    tweets = SentimentAnalyzer.main("#depressed")
    anxiety = SentimentAnalyzer.main("#anxiety")
    tweets.extend([x for x in anxiety if x not in tweets])
    training = []
    for x in tweets:
      training.append(list(x.values())[0])

    xyz =  getTimeline("@realDonaldTrump")
    for y in xyz:
       print(y)

  @staticmethod
  def getTimeline(username):
    timeline = []
    api = GetTimeline().api
    for status in tweepy.Cursor(api.user_timeline, screen_name = username,).items():
      timeline.append(status)

    return timeline

def main():
  GetTimeline().getTraining()


if __name__ == "__main__":
    main()










