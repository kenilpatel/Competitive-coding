import heapq


class Solution(object):
    def get(self):
        return 0

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict_count = defaultdict(self.get)
        for n in nums:
            dict_count[n] += 1
        pair = []
        for key in dict_count.keys():
            pair.append((-dict_count[key], key))
        heapq.heapify(pair)
        ans = []
        while k != 0:
            ans.append(heapq.heappop(pair)[1])
            k -= 1
        return ans
