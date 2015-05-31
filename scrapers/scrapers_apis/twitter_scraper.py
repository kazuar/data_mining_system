
from data_mining_system import settings

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

class TwitterScraper(object):
    def __init__(self):
        self._connection = settings.mongodb_connection
        

