class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            x = -x
            x = str(x)[::-1]
            x = -int(x)
            return x if x >= -2**31 else 0
        else:
            x = str(x)[::-1]
            x = int(x)
            return x if x <= 2**31 - 1 else 0
