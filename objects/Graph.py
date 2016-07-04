class Graph:
    def __init__(self, data):
        self.data = data

    def get_area_name(self):
        return self.data['area_name']

    def get_average_values_graph_url(self):
        return self.data['average_values_graph_url']

    def get_value_ranges_graph_url(self):
        return self.data['value_ranges_graph_url']

    def get_value_trend_graph_url(self):
        return self.data['value_trend_graph_url']

    def get_area_values_url(self):
        return self.data['area_values_url']

    def get_bounding_box(self):
        return self.data['bounding_box']
