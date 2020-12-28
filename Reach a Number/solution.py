class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        step = 0
        sum_ex = 0
        while True:
            step = step + 1
            sum_ex = sum_ex + step
            if sum_ex >= target:
                break
        if sum_ex == target:
            return step
        else:
            delta = sum_ex - target
            if delta % 2 == 0:
                return step
            else:
                if (delta + step + 1) % 2 == 0:
                    return step + 1
                else:
                     return step + 2