import requests
import time


class Object:
    def __init__(self, **entries):
        self.__dict__.update(entries)


class Zoopla:
    def __init__(self, api_key, debug=False, wait_on_rate_limit=False):
        self.debug = debug
        self.url = 'http://api.zoopla.co.uk/api/v1/'
        self.api_key = api_key
        self.wait_on_rate_limit = wait_on_rate_limit

    def local_info_graphs(self, area):
        return Object(**self._call('local_info_graphs.js', {
            'area': area
        }))

    def get_session_id(self):
        response = self._call('get_session_id.json?')
        return response['session_id']

    def zed_index(self, area, output_type='outcode'):
        return Object(**self._call('zed_index.json?', {
            'area': area,
            'output_type': output_type
        }))

    def area_value_graphs(self, area, size='medium'):
        return Object(**self._call('area_value_graphs.json?', {
            'area': area,
            'size': size
        }))

    def search_property_listings(self, params):
        c = self._call('property_listings.json?', params)
        result = []
        [result.append(Object(**r)) for r in c['listing']]
        return result

    def average_sold_prices(self, params):
        return Object(**self._call('average_sold_prices.json?', params))

    def get_average_area_sold_price(self, params):
        return Object(**self._call('average_area_sold_price.json?', params))

    def auto_complete(self, search_term, search_type='properties'):
        return Object(**self._call('geo_autocomplete.json?', {
            'api_key': self.api_key,
            'search_term': search_term,
            'search_type': search_type
        }))

    def area_zed_indices(self, params):

        return Object(**self._call('zed_indices.json', params))

    def _call(self, action, params=None):
        params.update({'api_key': self.api_key})
        r = requests.get(self.url + action, params)
        if r.status_code == 200:
            if self.debug:
                print(r.json())
                print(r.url)
            return r.json()
        else:
            if self.debug:
                print(r.json())
                print(r.url)
            if r.status_code == 403 and self.wait_on_rate_limit:
                print('Rate limit reached. Sleeping for 1 hour.')
                time.sleep(3605)
                self._call(self.url + action, params)
            else:
                raise ZooplaException(str(r.status_code), r.reason, r.text)


class ZooplaException(Exception):
    def __init__(self, status_code, reason, text):
        self.status_code = status_code
        self.reason = reason
        self.text = text

    def __str__(self):
        return "Zoopla returned an error: " + str(self.status_code) + " - " + self.reason + " - " + self.text
