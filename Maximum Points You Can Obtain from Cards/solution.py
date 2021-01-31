class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        s = n - k
        low = 0
        high = low + s
        sum_till = sum(cardPoints[low:high])
        mini = sum_till
        while high < n:
            sum_till = sum_till - cardPoints[low] + cardPoints[high]
            if sum_till < mini:
                mini = sum_till
            low = low + 1
            high = high + 1
        return sum(cardPoints) - mini
