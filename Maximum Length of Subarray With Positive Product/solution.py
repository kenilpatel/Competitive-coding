class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mul = 1
        for i,ele in enumerate(nums):
            if nums[i] != 0:
                if (mul > 0 and nums[i] > 0) or (mul < 0 and nums[i] < 0):
                    mul = 1
                else:
                    mul = -1
                nums[i] = mul
                mul = nums[i]
            else:
                mul = 1
        neg_index = float('inf')
        ans = 0
        last_zero = 0
        for i,ele in enumerate(nums):
            if ele < 0:
                if neg_index != float('inf'):
                    ans = max(ans,i - neg_index) 
                neg_index = min(neg_index,i)
            elif ele > 0:
                ans = max(ans,i - last_zero + 1)
            else:
                last_zero = i + 1
                neg_index = float('inf') 
        return ans
                
            
