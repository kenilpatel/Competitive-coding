class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        flag = 0
        for i in range(len(nums) - 1, -1, -1):
            m = nums[i]
            idx = -1
            if i + 1 < len(nums):
                for j in range(i + 1, len(nums)):
                    if nums[j] > m:
                        idx = j
                if idx != -1:
                    nums[i], nums[idx] = nums[idx], nums[i]
                    flag = 1
                    break
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[j] > nums[k]:
                    nums[j], nums[k] = nums[k], nums[j]
        if flag == 0:
            nums.sort()
