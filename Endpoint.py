class Endpoint:
    def __init__(self, data_center_latency_, data_center_, cache_servers_=[]):
        self.data_center_latency = data_center_latency_
        self.data_center = data_center_
        self._cache_servers = cache_servers_
        self._videos = []

        self.__sort_cache_servers()
        self.sort_videos()

    def __sort_cache_servers(self):
        self._cache_servers.sort(key=lambda x: x[1] / self.data_center.memory_per_cache_server)

    def add_video(self, number_of_requests, video_index, video_size):
        self._videos.append([number_of_requests, video_index, video_size])

    def sort_videos(self):
        self._videos.sort(key=lambda x: x[2] / x[0])

    def knapsack(self, items, weight):
        items = list(enumerate(items))
        sorted_items = sorted(items, key=lambda arr: arr[1][1] / arr[1][0])
        result_items = []
        current_weight = 0
        total_value = 0
        print(sorted_items)
        weight_threshold = weight # * lerp(0.6, 0.9, len(items) / 200)

        for i in range(len(sorted_items)):
            print(result_items, current_weight, total_value)
            weight_diff = weight - current_weight
            if current_weight < weight_threshold:
                if weight_diff > sorted_items[i][1][1]:
                    result_items.append(sorted_items[i][0])
                    current_weight += sorted_items[i][1][1]
                    total_value += sorted_items[i][1][0]

        # brut = brut_knapsack(sorted_items[end_index:], weight - current_weight)

        return total_value, result_items
