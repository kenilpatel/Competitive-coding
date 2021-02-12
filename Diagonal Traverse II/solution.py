class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        diagonal = defaultdict(lambda: [])
        n = len(nums)
        for i in range(0, n):
            m = len(nums[i])
            for j in range(0, m):
                diagonal[i + j].insert(0, nums[i][j])
        ans = []
        for key, item in diagonal.items():
            ans += item
        return ans
