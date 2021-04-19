class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans = 0
        o = 0 
        e = 1
        n = len(arr)
        for i in range(1,n):
            arr[i] += arr[i - 1]
        for i in range(0,n):
            if arr[i] % 2 == 0:
                ans += o
                e += 1
            else:
                ans += e
                o += 1
        return ans % (10**9 + 7)
            
