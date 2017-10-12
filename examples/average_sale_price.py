from zoopla import Zoopla

zoopla = Zoopla(api_key='your_api_key')

average = zoopla.average_area_sold_price({'area': 'SW11'})
print(average.average_sold_price_7year)
print(average.average_sold_price_5year)
