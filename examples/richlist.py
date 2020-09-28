from zoopla import Zoopla

zoopla = Zoopla(api_key='')

rl = zoopla.property_rich_list({'area': 'SW11'})

for l in rl.highest:
    print(l.name)
    print(l.zed_index)
    print(l.details_url)
