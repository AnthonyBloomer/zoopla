class Listing:
    def __init__(self, data):
        self.data = data

    def get_listing_status(self):
        return self.data['listing_status']

    def get_street_name(self):
        return self.data['street_name']

    def get_outcode(self):
        return self.data['outcode']

    def get_county(self):
        return self.data['county']

    def get_price(self):
        return self.data['price']

    def get_listing_id(self):
        return self.data['listing_id']
