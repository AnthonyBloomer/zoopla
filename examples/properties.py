from zoopla import Zoopla

zoopla = Zoopla(api_key='your_api_key')

search = zoopla.property_listings({
    'maximum_beds': 2,
    'page_size': 100,
    'listing_status': 'sale',
    'area': 'Blackley, Greater Manchester'
})

for result in search.listing:
    print(result.price)
    print(result.description)
    print(result.image_url)
