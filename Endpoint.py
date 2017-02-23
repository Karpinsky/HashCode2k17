from CacheServer import CacheServer


class Endpoint:
    def __init__(self, data_center_latency_, data_center_, cache_servers_=[]):
        self.data_center_latency = data_center_latency_
        self.data_center = data_center_
        self._cache_servers = cache_servers_
        self._videos = []

    def __sort_cache_servers(self):
        self._cache_servers.sort(key=lambda x: x[1] / self.data_center.memory_per_cache_server)

    def add_video(self, number_of_requests, video_index, video_size):
        self._videos.append([number_of_requests, video_index, video_size])

    def sort_videos(self):
        self._videos.sort(key=lambda x: x[2] / x[0])

    def knapsack(self):

        # [(0, 100), (2, 200), (1, 200)]
        for i in range(len(self._cache_servers)):
            cache_server = CacheServer(self.data_center_latency, self._cache_servers[i][1])
            cache_server_memory_left = self.data_center.memory_per_cache_server
            self.data_center.add_cache_server(cache_server)

            for j in range(len(self._videos)):
                if self._videos[j] is not None and self._videos[j][2] <= cache_server_memory_left:
                    cache_server_memory_left -= self._videos[j][2]
                    cache_server.cash_video(self._videos[j])
                    self._videos[j] = None

    def estimate_for_point(self):
        self.__sort_cache_servers()
        self.sort_videos()
        self.knapsack()