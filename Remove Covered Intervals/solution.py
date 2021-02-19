class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        ans = []
        l = 0
        for i in range(0, len(intervals)):
            covered = False
            for j in range(0, len(intervals)):
                if intervals[j][0] <= intervals[i][0] and intervals[i][1] <= intervals[j][1] and j != i:
                    covered = True
            if covered == False:
                ans.append(intervals[i])
                l += 1
        return l
