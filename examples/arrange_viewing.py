from zoopla import Zoopla

zoopla = Zoopla(api_key='your_api_key')

session = zoopla.get_session_id()

arrange_viewing = zoopla.arrange_viewing({
    'session_id': session,
    'listing_id': 44863256,
    'name': 'Tester',
    'email': "zoopla_developer@mashery.com",
    'phone': '01010101',
    'phone_type': 'work',
    'best_time_to_call': 'anytime',
    'message': 'Hi, I seen your listing on zoopla.co.uk and I would love to arrange a viewing!'

})

if 'success' in arrange_viewing and arrange_viewing.success == 1:
    print("Advertiser contacted successfully.")
