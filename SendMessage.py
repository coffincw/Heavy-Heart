from time import time
import os
import pymongo
import SentimentAnalyzer
import tweepy
from ConfigureMessage import generate_dm_text

consumer_token = os.environ['n4zRm3xuVoYoBHDLbSSqCxlII']
consumer_secret = os.environ['i2bxYM53rVNv0NFnO4iALdUYUDXHSEp9JARjpSu6290B5W6BLj']
access_token = os.environ['3265727682-sWioD71Vv1zJie1KCERyHZWgzCdDsGAy3lzdLJA']
access_token_secret = os.environ['Ir9vMlPyiJwafcqXOiRJgtdWpev2VU3rI0Z2MWXlJ79SV']

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)

def get_username(ids):
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    user_data = user = api.get_user(ids)
    return user_data.name

def send_direct_message(to_userid):
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    first_name = get_username(to_userid).split(' ')[0]
    dm_text = generate_dm_text(first_name)
    api.send_direct_message(to_userid, text=dm_text)