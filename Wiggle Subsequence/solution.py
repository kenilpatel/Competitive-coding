class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1: 
            return n
        elif n == 2:
            if nums[0] != nums[1]:
                return 2
            else:
                return 1
        else:
            diff = []
            for i in range(0,n - 1):
                diff.append(nums[i + 1] - nums[i])
            print(diff)
            pos = 0 
            neg = 0 
            for i,ele in enumerate(diff):
                if ele > 0:
                    diff[i] = 1 + neg
                    pos = max(pos,diff[i])
                elif ele < 0:
                    diff[i] = 1 + pos
                    neg = max(neg,diff[i]) 
                else:
                    diff[i] = 0
            return max(diff) + 1
