import collections


class Solution(object):
    dict = None

    def getval(self):
        return -99

    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        target = sum(nums) - x
        start = 0
        max_l = 0
        sum_d = {}
        sum_d[-1] = 0
        s = 0
        if target == 0:
            return len(nums)
        for i in range(0, len(nums)):
            s = s + nums[i]
            sum_d[i] = s
        for i in range(1, len(nums)):
            if nums[i] > target:
                start = i + 1
            else:
                while sum_d[i] - sum_d[start - 1] > target:
                    start = start + 1
            if i - start + 1 > max_l and sum_d[i] - sum_d[start - 1] == target:
                max_l = i - start + 1
        if max_l == 0:
            return -1
        return len(nums) - max_l
