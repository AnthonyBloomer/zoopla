import pytest

from zoopla.api import Zoopla


@pytest.fixture
def client(request):
    api_key = request.config.getoption("--api_key")
    return Zoopla(api_key=api_key)


def test_area_value_graphs(client):
    area_graphs = client.area_value_graphs(params={
        'area': 'SW11',
        'size': 'medium'
    })
    assert area_graphs.area_name == 'SW11'
    assert area_graphs.area_values_url == 'http://www.zoopla.co.uk/home-values/london/sw11/battersea-clapham-junction'  # noqa


def test_get_average_area_sold_price(client):
    averages = client.average_area_sold_price(params={
        'postcode': 'SW11',
        'output_type': 'outcode'
    })
    assert averages.area_name == 'SW11'


def test_search_property_listings(client):
    result = client.property_listings({
        'maximum_beds': 2,
        'page_size': 100,
        'listing_status': 'sale',
        'area': 'Blackley, Greater Manchester'
    })

    first = result.listing[0]
    assert first.listing_status == 'sale'


def test_local_info_graphs(client):
    local_graphs = client.local_info_graphs(params={
        'area': 'SW11'}
    )
    assert 'people_graph_url' in local_graphs
    assert local_graphs.country == 'England'
    assert local_graphs.area_name == 'SW11'


def test_zed_index(client):
    zed_result = client.zed_index(params={
        'area': 'SW11',
        'output_type': 'outcode'
    })
    assert zed_result.country == 'England'


def test_area_zed_indices(client):
    area_zed_indices = client.area_zed_indices(params={
        'area': 'Blackley, Greater Manchester',
        'output_type': 'area',
        'area_type': 'streets',
        'order': 'ascending',
        'page_number': 1,
        'page_size': 10
    })
    assert area_zed_indices.town == 'Manchester'


def test_auto_complete(client):
    auto_complete = client.geo_autocomplete(params={
        'search_term': 'SW11',
        'search_type': 'properties'
    })
    assert auto_complete.suggestions[0].value == 'SW11 1AD'  # noqa
