
from data_mining_system import settings

from instagram.client import InstagramAPI

from utils import text_utils

MAX_RESULTS = 20
MAX_DISTANCE = 5000

class InstagramScraper(object):
    def __init__(self):
        self._connection = settings.mongodb_connection
        self._config = self._connection.data_mining_system.consts.find_one({"name": "instagram"})
        client_id = str(self._config["access_keys"][0]["client_id"])
        client_secret = str(self._config["access_keys"][0]["client_secret"])
        self._api = InstagramAPI(client_id = client_id, client_secret = client_secret)
        self._max_results = self._config.get("max_results", MAX_RESULTS)
        self._max_distance = self._config.get("max_distance", MAX_DISTANCE)

    def find_location(self, q, lat, lng, source_name = None, source_id = None):
        arguments = dict(
            q = q,
            count = self._max_results,
            distance = self._max_distance,
            lat = lat,
            lng = lng,
        )
        if source_name == "foursquare":
            arguments["FOURSQUARE_V2_ID"] = source_id
        elif source_name =="facebook":
            arguments["FACEBOOK_PLACES_ID"] = source_id

        results = self._api.location_search(**arguments)
        return results

    def find_locations(self, poi_data):
        source_ids = poi_data.get('source_ids', {})
        foursquare_ids = source_ids.get('foursquare', [])
        facebook_ids = source_ids.get('facebook', [])
        poi_name = text_utils.clean_text(poi_data["name"])
        lat, lng = poi_data["coordinates"]
        results = self.find_location(poi_name, lat, lng)
        return results

    def search_poi(self, poi_data):
        return None

    def match_poi(self, poi_data, search_results):
        return None

    def get_poi(self, poi_data):
        return None

    def find_poi(self, poi_data):
        return None

