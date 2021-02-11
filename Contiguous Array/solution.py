class Solution(object):
    def get(self):
        return float('inf')

    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        k = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        mlen = 0
        index_d = defaultdict(self.get)
        index_d[0] = -1
        index_d[nums[0]] = min(index_d[nums[0]], 0)
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
            index_d[nums[i]] = min(index_d[nums[i]], i)
            cur_len = i - index_d[nums[i] - k]
            mlen = max(mlen, cur_len)
        return mlen
