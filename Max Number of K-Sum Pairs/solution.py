import collections


class Solution(object):
    def getval(self):
        return 0

    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count_dict = defaultdict(self.getval)
        for n in nums:
            count_dict[n] += 1
        pairs = 0
        for n in nums:
            rest = k - n
            if count_dict[n] > 0 and count_dict[rest] > 0 and n != rest:
                pairs += 1
                count_dict[n] -= 1
                count_dict[rest] -= 1
            if n == rest:
                if count_dict[n] > 1:
                    pairs += 1
                    count_dict[n] -= 1
                    count_dict[rest] -= 1
        return pairs
