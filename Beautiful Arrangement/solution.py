class Solution(object):
    n = None
    cnt = 0
    memo = None

    def get(self):
        return []

    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.n = n
        self.cnt = 0
        arrangement = [0] * (n + 1)
        self.memo = defaultdict(self.get)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if j % i == 0 or i % j == 0:
                    self.memo[i].append(j)
        self.dfs(arrangement, 1)
        return self.cnt

    def dfs(self, arrangement, numtoplace):
        for i in self.memo[numtoplace]:
            if arrangement[i] == 0:
                if numtoplace == self.n:
                    self.cnt += 1
                else:
                    self.dfs(arrangement[0:i] + [numtoplace] +
                             arrangement[i + 1:], numtoplace + 1)
