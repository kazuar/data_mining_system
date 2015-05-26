
import wikipedia
import traceback

class WikipediaScraper(object):

    def search_by_geocoordinates(geo_lat, geo_lon, poi_name = None):
        results = wikipedia.geosearch(geo_lat, geo_lon, poi_name)
        return results

    def search_by_name(poi_name, geo_lat, geo_lon):
        results = []
        wikipedia_results = wikipedia.search(poi_name)
        for wikipedia_result in wikipedia_results:
            try:
                geo_coordinates = wikipedia_result.coordinates
            except Exception:
                traceback.print_exc()
                continue
            if geo_coordinates:
                results.append(wikipedia_result)
        return results

    def find_poi(poi_data):
        poi_name = poi_data.get('name', None)
        if not poi_name:
            return None
        lat = poi_data.get('lat')
        lon = poi_data.get('lon')
        if lat and lon:
            results = search_by_geocoordinates(lat, lon, poi_name)
        return results
