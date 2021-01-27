class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = list(str(num))
        for i in range(0, len(num)):
            index = -1
            for j in range(i + 1, len(num)):
                if num[i] < num[j]:
                    if index == -1:
                        index = j
                    if num[index] <= num[j]:
                        index = j
            if index != -1:
                num[i], num[index] = num[index], num[i]
                break
        return "".join(num)
