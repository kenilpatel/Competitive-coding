class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = []
        for i in range(0, n):
            nums.append(2*i + 1)
        if (n - 1) % 2 == 0:
            idx = (n - 1) // 2
            intn = nums[idx]
        else:
            idx = (n - 1) // 2
            intn = (nums[idx] + nums[idx + 1]) / 2
        # print(idx,nums,intn)
        num_op = 0
        for i in range(0, idx + 1):
            num_op += intn - nums[i]
        return num_op
