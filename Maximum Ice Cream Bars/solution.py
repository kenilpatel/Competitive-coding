class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs = sorted(costs)
        ans = 0
        while True and costs: 
            top = costs.pop(0)
            if top <= coins:
                coins -= top
            else:
                break
            ans += 1 
        return ans
