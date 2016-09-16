import requests


class Object:
    def __init__(self, **entries):
        self.__dict__.update(entries)


class Zoopla:
    def __init__(self, api_key):
        self.url = 'http://api.zoopla.co.uk/api/v1/'
        self.api_key = api_key

    def local_info_graphs(self, area):
        return Object(**self._call('local_info_graphs.json?', {
            'api_key': self.api_key,
            'area': area
        }))

    def get_session_id(self):
        response = self._call('get_session_id.json?', {
            'api_key': self.api_key
        })

        return response['session_id']

    def zed_index(self, area, output_type='outcode'):
        return Object(**self._call('zed_index.json?', {
            'api_key': self.api_key,
            'area': area,
            'output_type': output_type
        }))

    def area_value_graphs(self, area, size='medium'):
        return Object(**self._call('area_value_graphs.json?', {
            'api_key': self.api_key,
            'area': area,
            'size': size
        }))

    def search_property_listings(self, params):
        params.update({'api_key': self.api_key})
        c = self._call('property_listings.json?', params)
        result = []
        [result.append(Object(**r)) for r in c['listing']]
        return result

    def get_average_area_sold_price(self, area=None, postcode=None, output_type='outcode', area_type='streets'):
        return Object(**self._call('average_area_sold_price.json?', {
            'api_key': self.api_key,
            'postcode': postcode,
            'area': area,
            'output_type': output_type,
            'area_type': area_type
        }))

    def auto_complete(self, search_term, search_type='properties'):
        return Object(**self._call('geo_autocomplete.json?', {
            'api_key': self.api_key,
            'search_term': search_term,
            'search_type': search_type
        }))

    def area_zed_indices(self, area, area_type='streets', output_type='area', order='ascending', page_number=1,
                         page_size=10):
        return Object(**self._call('zed_indices.json', {
            'api_key': self.api_key,
            'area': area,
            'output_type': output_type,
            'area_type': area_type,
            'order': order,
            'page_number': page_number,
            'page_size': page_size

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
