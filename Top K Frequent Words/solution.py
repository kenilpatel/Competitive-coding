import heapq


class Solution(object):
    def get(self):
        return 0

    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        cnt = defaultdict(self.get)
        for w in words:
            cnt[w] -= 1
        cnt = zip(cnt.values(), cnt.keys())
        heapq.heapify(cnt)
        ans = []
        for i in range(0, k):
            ans.append(heapq.heappop(cnt)[1])
        return ans
