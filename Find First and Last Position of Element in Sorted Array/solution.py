class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        x = bisect.bisect_left(nums, target)
        y = bisect.bisect_right(nums, target) - 1
        if x >= len(nums):
            return [-1, -1]
        if nums[x] == target:
            return [x, y]
        else:
            return [-1, -1]
