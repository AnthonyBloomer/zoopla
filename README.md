# zoopla
A python wrapper for the Zoopla API.

## Examples

### Search
```python
zoopla = Zoopla('your_api_key')

search = self.zoopla.search_property_listings(params={
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

### Area Value Graphs

```python
area_graphs = zoopla.area_value_graphs('SW11')

print area_graphs.average_values_graph_url
print area_graphs.value_trend_graph_url

```

### Average Area Sold Price

```python
average = zoopla.get_average_area_sold_price('SW11')
print average.average_sold_price_7year
print average.average_sold_price_5year
```
