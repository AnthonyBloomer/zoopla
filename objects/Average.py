class Average:
    def __init__(self, data):
        self.data = data

    def get_area_name(self):
        return self.data['area_name']

    def get_number_of_sales_5year(self):
        return self.data['number_of_sales_5year']

    def get_average_sold_price_5year(self):
        return self.data['average_sold_price_5year']

    def get_number_of_sales_3year(self):
        return self.data['number_of_sales_3year']

    def get_average_sold_price_3year(self):
        return self.data['average_sold_price_3year']

    def get_number_of_sales_1year(self):
        return self.data['number_of_sales_1year']

    def get_average_sold_price_1year(self):
        return self.data['average_sold_price_1year']
