import requests
import time


class Object:
    def __init__(self, **entries):
        self.__dict__.update(entries)


class Zoopla:
    def __init__(self, api_key, debug=False, wait_on_rate_limit=False):
        """
        :param api_key: Zoopla API Key
        :param debug: When set to true, we output the JSON response and URI.
        :param wait_on_rate_limit: When the rate limit is reached, we sleep for 1 hour before making a call to the API again.
        """
        self.debug = debug
        self.url = 'http://api.zoopla.co.uk/api/v1/'
        self.api_key = api_key
        self.wait_on_rate_limit = wait_on_rate_limit

    def local_info_graphs(self, area):

        """
        Generate a set of graphs of local info for an outcode (and optional incode) and return the URL to the generated image.
        :param area: string
        :return: object
        """

        return Object(**self._call('local_info_graphs.js', {
            'api_key': self.api_key,
            'area': area
        }))

    def get_session_id(self):
        """
        Obtain a session ID parameter for use with associated method calls.
        :return: string
        """
        response = self._call('get_session_id.json?', {
            'api_key': self.api_key
        })

        return response['session_id']

    def zed_index(self, area, output_type='outcode'):
        """
        Retrieve the Zoopla.co.uk Zed-Index! for a requested area.
        :param area: string
        :param output_type: string
        :return: object
        """
        return Object(**self._call('zed_index.json?', {
            'api_key': self.api_key,
            'area': area,
            'output_type': output_type
        }))

    def area_value_graphs(self, area, size='medium'):
        """
        Generate a graph of values for an outcode over the previous 3 months and return the URL to the generated image.
        :param area: string
        :param size: string
        :return: object
        """
        return Object(**self._call('area_value_graphs.json?', {
            'api_key': self.api_key,
            'area': area,
            'size': size
        }))

    def search_property_listings(self, params):
        """
        Retrieve property listings for a given area.
        :param params: array
        :return: object
        """
        params.update({'api_key': self.api_key})
        c = self._call('property_listings.json?', params)
        result = []
        [result.append(Object(**r)) for r in c['listing']]
        return result

    def average_sold_prices(self, postcode, output_type='county', area_type='streets', page_number=1, page_size=100,
                            ordering='descending'):
        """
         Retrieve the average sale price for a particular sub-area type within a particular area.
        :param postcode: string
        :param output_type: string
        :param area_type: string
        :param page_number: int
        :param page_size: int
        :param ordering: string
        :return: object
        """
        return Object(**self._call('average_sold_prices.json?', {
            'api_key': self.api_key,
            'postcode': postcode,
            'output_type': output_type,
            'area_type': area_type,
            'page_number': page_number,
            'page_size': page_size,
            'ordering': ordering
        }))

    def get_average_area_sold_price(self, county=None, area=None, postcode=None, output_type='outcode',
                                    area_type='streets'):
        """
        Retrieve the average sale price for houses in a particular area.
        :param county: string
        :param area: string
        :param postcode: string
        :param output_type: string
        :param area_type: string
        :return: object
        """
        return Object(**self._call('average_area_sold_price.json?', {
            'api_key': self.api_key,
            'postcode': postcode,
            'county': county,
            'area': area,
            'output_type': output_type,
            'area_type': area_type
        }))

    def auto_complete(self, search_term, search_type='properties'):
        """
        This method is for showing the auto suggestion for locations.
        :param search_term: string
        :param search_type: string
        :return: object
        """
        return Object(**self._call('geo_autocomplete.json?', {
            'api_key': self.api_key,
            'search_term': search_term,
            'search_type': search_type
        }))

    def area_zed_indices(self, area, area_type='streets', output_type='area', order='ascending', page_number=1,
                         page_size=10):
        """
        Retrieve a list of house price estimates for the requested area.
        :param area: string
        :param area_type: string
        :param output_type: string
        :param order: string
        :param page_number: int
        :param page_size: int
        :return: object
        """
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
        """
        Make a call to the Zoopla API and returns the JSON response.
        :param action: The Zoopla method
        :param params: The get parameters
        :return: Returns the JSON response
        """
        r = requests.get(self.url + action, params)

        if r.status_code == 200:

            if self.debug:
                print r.url
                print r.json()

            return r.json()
        else:
            print r.url
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
