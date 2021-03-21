class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pre_fix = defaultdict(lambda:0)
        pre_fix[0] = 1
        count = 0
        for i in range(1,len(nums)):
            nums[i] += nums[i - 1]  
        for i in nums: 
            target = i - k
            count += pre_fix[target]
            pre_fix[i] += 1
        return count
