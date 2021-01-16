class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sum(nums)
        step = 0
        while s != 0:
            for i in range(0,len(nums)):
                if nums[i] % 2 == 1:
                    nums[i] = nums[i] - 1
                    step = step + 1
                    s = s - 1
            for i in range(0,len(nums)):
                nums[i] = nums[i] / 2
            if s != s / 2:
                step = step + 1
                s = s / 2
        return step
