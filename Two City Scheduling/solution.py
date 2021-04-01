class Solution(object): 
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """ 
        def c(x,y):
            if x[1] - x[0] < y[1] - y[0]:
                return -1 
            else:
                return 1
        costs = sorted(costs,cmp = c,reverse = True)
        tot = 0
        n = len(costs) / 2
        for i in range(0,n):
            tot += costs[i][0]
        for i in range(n,n * 2):
            tot += costs[i][1]
        return tot
            
