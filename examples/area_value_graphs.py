from zoopla import Zoopla

zoopla = Zoopla(api_key='your_api_key')

area_graphs = zoopla.area_value_graphs({'area': 'SW11'})

print(area_graphs.average_values_graph_url)
print(area_graphs.value_trend_graph_url)
