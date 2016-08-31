import requests
import unittest


class Object:
    def __init__(self, **entries):
        self.__dict__.update(entries)


class Zoopla:
    def __init__(self, api_key):
        self.url = 'http://api.zoopla.co.uk/api/v1/'
        self.api_key = api_key

    def local_info_graphs(self, area):
        return Object(**self._call('local_info_graphs.js', {
            'api_key': self.api_key,
            'area': area
        }))

    def zed_index(self, area, output_type='outcode'):
        return Object(**self._call('zed_index.js?', {
            'api_key': self.api_key,
            'area': area,
            'output_type': output_type
        }))

    def area_value_graphs(self, area, size='medium'):
        return Object(**self._call('area_value_graphs.js?', {
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

    def _call(self, action, params):
        r = requests.get(self.url + action, params)
        if r.status_code == 200:
            print r.url
            print r.json()
            return r.json()
        else:
            raise ZooplaException(str(r.status_code), r.reason, r.text)


class ZooplaTests(unittest.TestCase):
    def setUp(self):
        self.zoopla = Zoopla('')

    def test_area_value_graphs(self):
        area_graphs = self.zoopla.area_value_graphs('SW11')
        area_name = area_graphs.area_name
        self.assertEquals(area_name.strip(), 'SW11')

    def test_get_average_area_sold_price(self):
        averages = self.zoopla.get_average_area_sold_price('SW11')
        self.assertEqual(averages.area_name.strip(), 'SW11')

    def test_search_property_listings(self):
        search = self.zoopla.search_property_listings(params={
            'maximum_beds': 2,
            'page_size': 100,
            'listing_status': 'sale',
            'area': 'Blackley, Greater Manchester'
        })

        first = search[0]
        self.assertEquals(first.listing_status, 'sale')

    def test_local_info_graphs(self):
        local_graphs = self.zoopla.local_info_graphs('SW11')
        country = local_graphs.country
        self.assertEquals(country, 'England')

    def test_zed_index(self):
        zed = self.zoopla.zed_index('SW11')
        country = zed.country
        self.assertEqual(country, 'England')


class ZooplaException(Exception):
    def __init__(self, status_code, reason, text):
        self.status_code = status_code
        self.reason = reason
        self.text = text

    def __str__(self):
        return "Zoopla returned an error: " + str(self.status_code) + " - " + self.reason + " - " + self.text


if __name__ == '__main__':
    unittest.main()
