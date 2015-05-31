
from data_mining_system import settings

import tweepy

class TwitterScraper(object):
    def __init__(self):
        self._connection = settings.mongodb_connection
        self._config = self._connection.data_mining_system.consts.find_one({"name": "twitter"})
        self._auth = self._create_auth(self._config)
        self._api = tweepy.API(self._auth)

    def _create_auth(self, config):
        access_key_settings = config["access_keys"][0]
        auth = tweepy.OAuthHandler(access_key_settings["api_key"], access_key_settings["api_secret"])
        auth.set_access_token(access_key_settings["access_token"], access_key_settings["access_token_secret"])
        return auth

    def search_poi(self, poi_data):
        return None

    def match_poi(self, poi_data, search_results):
        return None

    def get_poi(self, poi_data):
        return None

    def find_poi(self, poi_data):
        search_results = self.search_poi(poi_data)
        matching_result = self.match_poi(poi_data, search_results)
        pois_data = self.get_poi(matching_result)
        return pois_data
