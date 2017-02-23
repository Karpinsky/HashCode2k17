from DataCenter import DataCenter


class Endpoint:
    def __init__(self, data_center_latency_, data_center_, cache_servers_=[]):
        self.data_center_latency = data_center_latency_
        self.data_center = data_center_
        self._cache_servers = cache_servers_
        self._videos = []

        self.__sort_cache_servers()

    def __sort_cache_servers(self):
        self._cache_servers.sort(key=lambda x: x[1] / self.data_center.memory_per_cache_server)

    def add_video(self, number_of_requests, video_index, video_size):
        self._videos.append([number_of_requests, video_index, video_size])

    def sort_videos(self):
        self._videos.sort(key=lambda x: x[2] / x[0])

if __name__ == '__main__':
    endpoint_1 = Endpoint(1000, DataCenter(5, 2, 4, 3, 100), [(0, 100), (2, 200), (1, 200)])
