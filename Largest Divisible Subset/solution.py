class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        count = [0] * n
        index = [-1] * n
        nums = sorted(nums)
        endi = -1
        gc = 0
        for i in range(0,n):
            maxc = 0 
            idx = -1
            for j in range(0,i):
                if nums[i] % nums[j] == 0:
                    if maxc < count[j]:
                        maxc = count[j]
                        idx = j
            count[i] = maxc + 1
            index[i] = idx
            if gc < count[i]:
                gc = count[i]
                endi = i
        ans = []
        while endi != - 1:
            ans.insert(0,nums[endi])
            endi = index[endi]
        return ans
