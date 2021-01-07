class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        arr = []
        N = len(nums)
        for i in range(N):
            cur = 0
            for j in range(i, N):
                cur = cur + nums[j]
                arr.append(cur)
        arr.sort()
        return sum(arr[left - 1:right]) % (10**9 + 7)
