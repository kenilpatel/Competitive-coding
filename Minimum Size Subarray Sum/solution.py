class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(1, n):
            nums[i] = nums[i] + nums[i - 1]
        min_len = float('inf')
        for i in range(0, n):
            search = nums[i] - s
            if search == 0:
                min_len = min(min_len, i + 1)
            elif search > 0 and i >= 1:
                index = bisect.bisect_right(nums[0:i], search)
                v1 = index - 1
                v2 = index
                v3 = index + 1
                maxi = 0
                if v1 >= 0 and nums[v1] <= search:
                    maxi = max(maxi, v1)
                if v2 < n and nums[v2] <= search:
                    maxi = max(maxi, v2)
                if v3 < n and nums[v3] <= search:
                    maxi = max(maxi, v3)
                min_len = min(min_len, i - maxi)
            elif search > 0 and i == 0:
                min_len = min(min_len, i + 1)
        if min_len == float('inf'):
            return 0
        return min_len
