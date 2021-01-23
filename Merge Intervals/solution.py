class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        for i in range(0, len(intervals)):
            intervals[i] = tuple(intervals[i])
        intervals = sorted(intervals)
        for i in range(0, len(intervals)):
            intervals[i] = list(intervals[i])
        print(intervals)
        for i in range(1, len(intervals)):
            intervals[i][0] = max(intervals[i][0], intervals[i-1][1])
            intervals[i][1] = max(intervals[i][1], intervals[i-1][1])
        merged = [intervals[0]]
        ind = 0
        for i in range(1, len(intervals)):
            if merged[ind][1] == intervals[i][0]:
                merged[ind][1] = max(merged[ind][1], intervals[i][1])
            else:
                merged.append(intervals[i])
                ind += 1
        return merged
