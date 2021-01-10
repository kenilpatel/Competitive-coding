import math


class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        first_monday = 1
        prev = 1
        balance = 0
        for i in range(1, n + 1):
            # print(prev)
            balance = balance + prev
            prev = prev + 1
            if i % 7 == 0:
                prev = first_monday + 1
                first_monday = first_monday + 1
        return balance
