class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time,tweetId))
        self.time +=1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = self.following[userId] | {userId}
        for uid in users:
            if self.tweets[uid]:
                i = len(self.tweets[uid]) - 1
                time, tid = self.tweets[uid][i]
                heapq.heappush(heap,(-time,tid,uid,i))

        res = []
        while heap and len(res) < 10:
            time,tid,uid,i = heapq.heappop(heap)
            res.append(tid)
            if i>0:
                i-=1
                time2,tid2 = self.tweets[uid][i]
                heapq.heappush(heap,(-time2,tid2,uid,i))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
