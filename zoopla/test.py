import unittest
from zoopla import Zoopla


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

    def test_area_zed_indices(self):
        a = self.zoopla.area_zed_indices(area='Blackley, Greater Manchester')
        self.assertEqual(a.town, 'Manchester')

    def test_auto_complete(self):
        a = self.zoopla.auto_complete('SW')
        self.assertEqual(a.suggestions[0]['value'], 'SW1A 0PW')
