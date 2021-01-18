import math
import copy


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        dl = []
        n = 0
        original = copy.deepcopy(x)
        reverse = 0
        if x < 0:
            return False
        while x != 0:
            dl.append(x % 10)
            n += 1
            x = int(math.floor(x / 10))
        for d in dl:
            reverse += d * 10 ** (n - 1)
            n = n - 1
        return reverse == original
