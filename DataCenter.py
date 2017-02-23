from Endpoint import Endpoint


class DataCenter:

    def __init__(self, number_of_videos, number_of_endpoints, number_of_request__descriptions, number_of_cashes, memory_per_cache_server):
        self.number_of_videos = number_of_videos
        self.number_of_endpoints = number_of_endpoints
        self.number_of_request_descriptions = number_of_request__descriptions
        self.number_of_cashes = number_of_cashes
        self.memory_per_cache_server = memory_per_cache_server

        self.endpoints = []

        self.parse_data()

    def parse_data(self):
        self.endpoints.append(Endpoint(1000, self, [(0, 100), (2, 200), (1, 200)]))

data_center = DataCenter(5, 2, 4, 3, 100)