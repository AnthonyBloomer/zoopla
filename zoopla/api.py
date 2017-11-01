import logging

import requests

from .exceptions import (
    ZooplaAPIException, ResponseFormatException, RequestFormatException)
from .schemas import (
    PropertyListingResultSchema, LocalInfoGraphsResultSchema, ZedIndexResultSchema,
    AreaZedIndicesResultSchema, AutoCompleteResultSchema,
    AreaValueGraphsResultSchema,
    AverageSoldPricesBaseResultSchema, AverageAreaSoldPriceResultSchema,
    BaseRequestSchema, SearchPropertyListingRequestSchema, ZedIndexRequestSchema,
    AreaZedIndicesRequestSchema, AutocompleteRequestSchema,
    AreaValueGraphsRequestSchema, AverageSoldPriceRequestSchema, RefineEstimateSchema, RefineEstimateResultSchema,
    ArrangeViewingSchema, ArrangeViewingResultSchema
)

logging.basicConfig()
logger = logging.getLogger(__file__)


class Zoopla(object):
    API_URL = 'http://api.zoopla.co.uk/api/v1/'

    def __init__(self, api_key):
        self.api_key = api_key

    def _api_call(self, action, params=None):
        if not params:
            params = {}

        params.update({'api_key': self.api_key})
        response = requests.get(
            self.API_URL + action, params)

        if response.ok:
            return response.json()
        else:
            raise ZooplaAPIException(
                str(response.status_code),
                response.reason,
                response.text)

    def _base_call(self, action, request_schema, result_schema, parameters):
        request_errors = request_schema().validate(parameters)

        if request_errors:
            logger.warning(parameters)
            raise RequestFormatException(request_errors)

        response = self._api_call(action, parameters)
        result, errors = result_schema().load(response)

        if errors:
            logger.warning(response)
            raise ResponseFormatException(errors)

        return result

    def zed_index(self, params):
        """
        Retrieve the Zoopla.co.uk Zed-Index! for a requested area.
        """
        return self._base_call(
            action='zed_index.json',
            request_schema=ZedIndexRequestSchema,
            result_schema=ZedIndexResultSchema,
            parameters=params
        )

    def area_value_graphs(self, params):
        """
        Generate a graph of values for an outcode over the previous 3 months
        and return the URL to the generated image. Please note that
        the output type must always be "outcode" for this method
        and therefore an area sufficient to produce an outcode is required.
        """
        return self._base_call(
            action='area_value_graphs.json',
            request_schema=AreaValueGraphsRequestSchema,
            result_schema=AreaValueGraphsResultSchema,
            parameters=params
        )

    def property_rich_list(self, params):
        """
        Retrieve richlist values for a specific area.
        """
        raise NotImplementedError

    def average_area_sold_price(self, params):
        """
        Retrieve the average sale price for houses in a particular area.
        """
        return self._base_call(
            action='average_area_sold_price.json',
            request_schema=BaseRequestSchema,
            result_schema=AverageAreaSoldPriceResultSchema,
            parameters=params
        )

    def area_zed_indices(self, params):
        """
        Retrieve a list of house price estimates for the requested area.
        """
        return self._base_call(
            action='zed_indices.json',
            request_schema=AreaZedIndicesRequestSchema,
            result_schema=AreaZedIndicesResultSchema,
            parameters=params
        )

    def average_sold_prices(self, params):
        """
        Retrieve the average sale price for a particular sub-area
        type within a particular area.
        """
        return self._base_call(
            action='average_sold_prices.json',
            request_schema=AverageSoldPriceRequestSchema,
            result_schema=AverageSoldPricesBaseResultSchema,
            parameters=params
        )

    def property_listings(self, params):
        """
        Retrieve property listings for a given area.
        """
        return self._base_call(
            action='property_listings.json',
            request_schema=SearchPropertyListingRequestSchema,
            result_schema=PropertyListingResultSchema,
            parameters=params
        )

    def refine_estimate(self, params):
        """
        Request a more accurate Zoopla.co.uk Zed-Index
        based on extra data provided.
        """
        return self._base_call(
            action='refine_estimate.json',
            request_schema=RefineEstimateSchema,
            result_schema=RefineEstimateResultSchema,
            parameters=params
        )

    def arrange_viewing(self, params):
        """
        Submit a viewing request to an agent regarding a particular listing.
        """
        return self._base_call(
            action='arrange_viewing.json',
            request_schema=ArrangeViewingSchema,
            result_schema=ArrangeViewingResultSchema,
            parameters=params
        )

    def get_session_id(self):
        """
        Obtain a session ID parameter for use with associated method calls.
        """
        response = self._api_call('get_session_id.json?api_key=' + self.api_key)
        return response['session_id']

    def local_info_graphs(self, params):
        """
        Generate a set of graphs of local info for an outcode
        (and optional incode) and return the URL to the generated image.
        """
        return self._base_call(
            action='local_info_graphs.js',
            request_schema=BaseRequestSchema,
            result_schema=LocalInfoGraphsResultSchema,
            parameters=params
        )

    def geo_autocomplete(self, params):
        """
        This method is for showing the auto suggestion for locations.
        """
        return self._base_call(
            action='geo_autocomplete.json',
            request_schema=AutocompleteRequestSchema,
            result_schema=AutoCompleteResultSchema,
            parameters=params
        )
