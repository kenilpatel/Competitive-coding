class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        index = 0
        arr = [0] + arr
        for i in range(0, len(arr) - 1):
            if k - (arr[i + 1] - arr[i] - 1) >= 1:
                k = k - (arr[i + 1] - arr[i] - 1)
            else:
                return arr[i] + k
            index = index + 1
        if k >= 1:
            return arr[index] + k