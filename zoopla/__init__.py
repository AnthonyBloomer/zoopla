import requests
import unittest


class Graph:
    def __init__(self, data):
        self.data = data

    def get_area_name(self):
        return self.data['area_name']

    def get_average_values_graph_url(self):
        return self.data['average_values_graph_url']

    def get_value_ranges_graph_url(self):
        return self.data['value_ranges_graph_url']

    def get_value_trend_graph_url(self):
        return self.data['value_trend_graph_url']

    def get_area_values_url(self):
        return self.data['area_values_url']

    def get_bounding_box(self):
        return self.data['bounding_box']


class Listing:
    def __init__(self, data):
        self.data = data

    def get_listing_status(self):
        return self.data['listing_status']

    def get_street_name(self):
        return self.data['street_name']

    def get_outcode(self):
        return self.data['outcode']

    def get_county(self):
        return self.data['county']

    def get_price(self):
        return self.data['price']

    def get_listing_id(self):
        return self.data['listing_id']


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
        return self._call('average_area_sold_price.json?', {
            'api_key': self.api_key,
            'postcode': postcode,
            'area': area,
            'output_type': output_type,
            'area_type': area_type
        })

    def _call(self, action, params):
        r = requests.get(self.url + action, params)
        if r.status_code == 200:
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


class ZooplaTests(unittest.TestCase):
    def setUp(self):
        self.zoopla = Zoopla('')

    def test_area_value_graphs(self):
        area_graphs = self.zoopla.area_value_graphs('SW11')
        area_name = area_graphs.get_area_name()
        self.assertEquals(area_name.strip(), 'SW11')

    def test_get_average_area_sold_price(self):
        averages = self.zoopla.get_average_area_sold_price('SW11')
        self.assertEquals(averages['average_sold_price_1year'], '814144')

    def test_search_property_listings(self):
        search = self.zoopla.search_property_listings(params={
            'maximum_beds': 2,
            'page_size': 100,
            'listing_status': 'sale',
            'area': 'Blackley, Greater Manchester'
        })

        first = search[0]
        self.assertEquals(first.get_listing_status(), 'sale')

    def test_local_info_graphs(self):
        local_graphs = self.zoopla.local_info_graphs('SW11')
        area_name = local_graphs.get_area_name()
        self.assertEquals(area_name.strip(), 'SW11')


if __name__ == '__main__':
    unittest.main()
