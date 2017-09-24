# zoopla
A python wrapper for the Zoopla API.

Zoopla has launched an open API to allow developers to create applications using hyper local data on 27m homes, over 1m sale and rental listings, and 15 years of sold price data.

[Register](http://developer.zoopla.com/member/register/) for a user account and [apply](http://developer.zoopla.com/member/register/) for an instant API key.

Browse the [documentation](http://developer.zoopla.com/docs/) to understand how to use the API and the specifications for the individual APIs.

## Installation
```
pip install zoopla
```

## Tests

Install the dev requirements:

```sh
pip install -r dev-requirements.txt
```

Run py.test with your developer key (otherwise you won't be able to hit the live
API upon which these tests depend).

```sh
py.test --api-key=<you-api-key> tests/
```

## Examples

Retrieve property listings for a given area.
```python
from zoopla import Zoopla
zoopla = Zoopla(api_key='your_api_key')

search = zoopla.property_listings({
    'maximum_beds': 2,
    'page_size': 100,
    'listing_status': 'sale',
    'area': 'Blackley, Greater Manchester'
})

for result in search:
    print result.price
    print result.description
    print result.image_url
  
```

Retrieve a list of house price estimates for the requested area.

```python
zed_indices = zoopla.area_zed_indices({
    'area': 'Blackley, Greater Manchester',
    'output_type': 'area',
    'area_type': 'streets',
    'order': 'ascending',
    'page_number': 1,
    'page_size': 10
})

print zed_indices.town
print zed_indices.results_url
```


Generate a graph of values for an outcode over the previous 3 months and return the URL to the generated image.

```python
area_graphs = zoopla.area_value_graphs({'area': 'SW11'})

print area_graphs.average_values_graph_url
print area_graphs.value_trend_graph_url

```

Retrieve the average sale price for houses in a particular area.

```python
average = zoopla.get_average_area_sold_price({'area': 'SW11'})
print average.average_sold_price_7year
print average.average_sold_price_5year
```
