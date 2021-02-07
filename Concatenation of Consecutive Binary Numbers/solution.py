class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = ""
        for i in range(1, n + 1):
            ans += bin(i).replace("0b", "")
        return int(ans, 2) % 1000000007
