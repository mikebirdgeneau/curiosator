import tweepy
import secrets

from tweepy import OAuthHandler

consumer_key = secrets.consumer_key
consumer_secret = secrets.consumer_secret
access_token = secrets.access_token
access_secret = secrets.access_secret

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

