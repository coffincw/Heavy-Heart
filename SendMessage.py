from time import time
import tweepy
import SentimentAnalyzer
from ConfigureMessage import generate_dm_text
from SentimentAnalyzer import main



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

api = tweepy.API(auth)

neutral_negative_tweets = []
neutral_negative_tweets = main('#depressed')

def reach_out(tweets):
    names = []
    for x in tweets:
        test = x.split()[1]
        test = test[1].split()
        test = test[1:]
        names.append(''.join(test))
    ids = []
    for i in names:
        ids.append(get_identifier(i))
    send_message(ids)
    return ids

def send_message (ids):
    for i in ids:
        send_direct_message(i)


def get_identifier(name):
    user = api.get_user(screen_name = name)
    return user.id

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

print(reach_out(neutral_negative_tweets))