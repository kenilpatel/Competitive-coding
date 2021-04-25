class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i = 0 
        j = 0 
        count = 0
        n = len(nums)
        ans = 0
        while j < n:
            if nums[j] % 2 == 1:
                count += 1
                if count == k:
                    ans += 1
                    while i <= j and nums[i] % 2 == 0 :
                        ans += 1
                        i += 1 
                elif count > k:
                    count -= 1
                    i += 1
            j += 1
        while i < n  and nums[i] % 2 == 0 :
            ans += 1
            i += 1 
        return ans
        
