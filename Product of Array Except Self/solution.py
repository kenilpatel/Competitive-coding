class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        op = [1] * len(nums)
        op[0] = nums[0]
        for i in range(1, len(nums)):
            op[i] = nums[i] * op[i - 1]
        for j in range(len(nums) - 2, -1, -1):
            nums[j] = nums[j] * nums[j + 1]
        for i in range(0, len(nums)):
            if i - 1 >= 0 and i + 1 < len(nums):
                nums[i] = nums[i + 1] * op[i - 1]
            else:
                if i - 1 < 0:
                    nums[i] = nums[i + 1]
                else:
                    nums[i] = op[i - 1]
        return nums
