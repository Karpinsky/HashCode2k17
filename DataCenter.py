from Endpoint import Endpoint


class DataCenter:

    def __init__(self, number_of_videos, number_of_endpoints, number_of_request__descriptions, number_of_cashes, memory_per_cache_server):
        self.number_of_videos = number_of_videos
        self.number_of_endpoints = number_of_endpoints
        self.number_of_request_descriptions = number_of_request__descriptions
        self.number_of_cashes = number_of_cashes
        self.memory_per_cache_server = memory_per_cache_server

        self.all_videos_requests_quantity = 0

        self.endpoints = []
        self.cache_servers = []

        self.parse_data()

    def parse_data(self):
        with open("kittens.in", "r+") as file:
            print(file)



        endp = Endpoint(1000, self, [(0, 100), (2, 200), (1, 200)])
        self.endpoints.append(endp)
        endp.add_video(1500, 3, 30)
        self.all_videos_requests_quantity += 1500
        endp.add_video(1000, 0, 50)
        self.all_videos_requests_quantity += 1000
        endp.add_video(1000, 1, 50)
        self.all_videos_requests_quantity += 1000
        endp.add_video(500, 4, 110)
        self.all_videos_requests_quantity += 500
        endp.estimate_for_point()

    def add_cache_server(self, cache_server):
        self.cache_servers.append(cache_server)

    def get_total_score(self):
        total_score = 0
        for i in range(len(self.cache_servers)):
            total_score += self.cache_servers[i].estimate_value()

        return (total_score / self.all_videos_requests_quantity) * 1000


def reader(file_name):
    line_list = list()
    line_number = 0
    with open(file_name, 'r') as a_f:
        for i, l in enumerate(a_f):
            pass
        line_number = i
    line_number += 1

    with open(file_name, 'r') as a_file:
        for i in range(line_number):
            line = a_file.readline().split()
            line_list.append([int(x) for x in line])
    return line_list


def datacenter_creator(line_list):
    list_arguments = line_list[0]
    return DataCenter(list_arguments[0], list_arguments[1], list_arguments[2], list_arguments[3], list_arguments[4])


def endpoint_creator(line_list):
    enpoint_data = line_list[2:]
    endpoints_list = list()
    for i in range(line_list[0][1]):
        new_endPoint = Endpoint(endpoints_list[i][0])
        for j in range(i + 1, endpoints_list[i][1]):
            new_endPoint._cache_servers.append((endpoints_list[j][0], endpoints_list[j][1]))

data_center = DataCenter(5, 2, 4, 3, 100)

print(data_center.get_total_score())



