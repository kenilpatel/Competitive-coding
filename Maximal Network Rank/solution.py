class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        self.graph_c = defaultdict(lambda:0)
        self.graph_set = defaultdict(lambda:set())
        for i,j in roads:
            self.graph_c[i] += 1
            self.graph_c[j] += 1
            self.graph_set[i].add(j)
            self.graph_set[j].add(i)
        ans = 0 
        for i in range(n):
            for j in range(i + 1,n):
                tot = self.graph_c[i] + self.graph_c[j]
                if j in self.graph_set[i]:
                    tot -= 1
                ans = max(ans,tot)
        return ans
