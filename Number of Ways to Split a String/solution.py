import math
import functools


def ncr(n, r):
    return (math.factorial(n) / (math.factorial(r)
                                 * math.factorial(n - r)))


class Solution(object):
    def numWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        s = map(lambda x: int(x), s)
        sum_b = sum(s)
        print(sum_b)
        # print(sum_b)
        if sum_b == 0:
            return ncr(len(s) - 1, 2) % 1000000007
        if sum_b % 3 != 0:
            return 0
        no_of_1 = sum_b / 3
        # print(no_of_1)
        start = []
        end = []

        for i in range(1, len(s)):
            s[i] = (s[i] + s[i - 1])
        # print(s)
        s_f = 0
        e_f = s.index(no_of_1)
        s_s = s.index(no_of_1 + 1)
        e_s = s.index(no_of_1*2)
        s_t = s.index(no_of_1*2 + 1)
        e_t = s.index(no_of_1*3)
        # print(s_f,e_f,s_s,e_s,s_t,e_t)
        ans = 1
        ans = ans * (s_s - e_f) * (s_t - e_s)
        return ans % 1000000007
