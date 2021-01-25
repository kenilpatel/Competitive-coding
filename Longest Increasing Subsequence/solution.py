class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ml = [1] * len(nums)
        gm = 0
        for i in range(0, len(nums)):
            local = 0
            for j in range(0, i):
                if nums[j] < nums[i]:
                    if local < ml[j]:
                        local = ml[j]
            ml[i] = ml[i] + local
            if gm < ml[i]:
                gm = ml[i]
        return gm
