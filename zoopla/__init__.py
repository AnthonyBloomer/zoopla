import requests
from objects import Listing, Average, Graph


class Zoopla:
    def __init__(self, api_key):
        self.url = 'http://api.zoopla.co.uk/api/v1/'
        self.api_key = api_key

    def local_info_graphs(self, area):
        return Graph(self._call('local_info_graphs.js', {
            'api_key': self.api_key,
            'area': area
        }))

    def area_value_graphs(self, area, size='medium'):
        return Graph(self._call('area_value_graphs.js?', {
            'api_key': self.api_key,
            'area': area,
            'size': size
        }))

    def search_property_listings(self, params):
        params.update({'api_key': self.api_key})
        c = self._call('property_listings.json?', params)
        result = []
        [result.append(Listing(r)) for r in c['listing']]
        return result

    def get_average_area_sold_price(self, area=None, postcode=None, output_type='outcode', area_type='streets'):
        return Average(self._call('average_area_sold_price.json?', {
            'api_key': self.api_key,
            'postcode': postcode,
            'area': area,
            'output_type': output_type,
            'area_type': area_type
        }))

    def _call(self, action, params):
        r = requests.get(self.url + action, params)
        if r.status_code == 200:
            print r.json()
            return r.json()
        else:
            raise ZooplaException(str(r.status_code), r.reason, r.text)


class ZooplaException(Exception):
    def __init__(self, status_code, reason, text):
        self.status_code = status_code
        self.reason = reason
        self.text = text

    def __str__(self):
        return "Zoopla returned an error: " + str(self.status_code) + " - " + self.reason + " - " + self.text
