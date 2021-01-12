from sortedcontainers import SortedList


class Solution(object):
    def getcount(self):
        return 0

    def createSortedArray(self, instructions):
        """
        :type instructions: List[int]
        :rtype: int
        """
        s = SortedList()
        total = 0
        len_s = 0
        for num in instructions:
            left = s.bisect_left(num)
            right = len_s - s.bisect_right(num)
            total += min(left, right)
            len_s += 1
            s.add(num)
        return total % 1000000007
