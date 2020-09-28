from zoopla import Zoopla

zoopla = Zoopla(api_key='your_api_key')

zed_indices = zoopla.area_zed_indices({
    'area': 'Blackley, Greater Manchester',
    'output_type': 'area',
    'area_type': 'streets',
    'order': 'ascending',
    'page_number': 1,
    'page_size': 10
})

print(zed_indices.town)
print(zed_indices.results_url)
