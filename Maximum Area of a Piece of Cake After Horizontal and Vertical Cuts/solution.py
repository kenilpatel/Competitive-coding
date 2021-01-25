class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        max1 = 0
        max2 = 0
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(0)
        verticalCuts.append(w)
        horizontalCuts.sort()
        verticalCuts.sort()
        for i in range(0, len(horizontalCuts) - 1):
            if horizontalCuts[i + 1] - horizontalCuts[i] > max1:
                max1 = horizontalCuts[i + 1] - horizontalCuts[i]

        for i in range(0, len(verticalCuts) - 1):
            if verticalCuts[i + 1] - verticalCuts[i] > max2:
                max2 = verticalCuts[i + 1] - verticalCuts[i]

        return (max1 * max2) % (10**9 + 7)
