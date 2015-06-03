
from data_mining_system import settings

from instagram.client import InstagramAPI

class InstagramScraper(object):
    def __init__(self):
        self._connection = settings.mongodb_connection
        self._config = self._connection.data_mining_system.consts.find_one({"name": "instagram"})
        client_id = self._config["access_keys"][0]["client_id"]
        client_secret = self._config["access_keys"][0]["client_secret"]
        self._api = InstagramAPI(client_id = client_id, client_secret = client_secret)

    def search_poi(self, poi_data):
        return None

    def match_poi(self, poi_data, search_results):
        return None

    def get_poi(self, poi_data):
        return None
        
    def find_poi(self, poi_data):
        return None

