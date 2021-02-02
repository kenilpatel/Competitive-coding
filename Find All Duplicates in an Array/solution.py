class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(0, len(nums)):
            x = abs(nums[i]) - 1
            if nums[x] < 0:
                ans.append(abs(nums[i]))
            nums[x] = -nums[x]
        return ans
