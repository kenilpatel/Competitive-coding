class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        sell_price = [0]*n
        sell_price[n - 1] = prices[n - 1]
        for i in range(n - 2, -1, -1):
            sell_price[i] = max(prices[i], sell_price[i + 1])
        maxp = 0
        for i in range(0, n - 1):
            maxp = max(sell_price[i + 1] - prices[i], maxp)
        return maxp
