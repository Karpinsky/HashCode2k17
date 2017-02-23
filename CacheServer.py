class CacheServer:

    def __init__(self, data_center_latency, server_latency):
        self.cashed_videos = []
        self.data_center_latency = data_center_latency
        self.server_latency = server_latency

    def cash_video(self, video):
        self.cashed_videos.append(video)

    def estimate_value(self):
        score = 0
        for i in range(len(self.cashed_videos)):
            print(self.cashed_videos[i])
            score += self.cashed_videos[i][0] * (self.data_center_latency - self.server_latency)

        return score
