class Solution(object):
    memo = None
    job = None

    def get(self):
        return -1

    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        self.job = jobDifficulty
        self.memo = defaultdict(self.get)
        x = self.getdiffi(d, 0)
        return -1 if x == 2**31 else x

    def getdiffi(self, d, start):
        if self.memo[(start, d)] != -1:
            return self.memo[(start, d)]
        if len(self.job) < d:
            mt = 2 ** 31
            self.memo[(start, d)] = mt
            return 2**31
        if d == 1:
            mt = max(self.job[start:])
            self.memo[(start, d)] = mt
            return mt
        mt = 2**31
        mn = self.job[start]
        for i in range(start, len(self.job) - d + 1):
            if mn < self.job[i]:
                mn = self.job[i]
            # print(self.job[0:i+1],self.job[i+1:],mn)
            x = mn + self.getdiffi(d - 1, i+1)
            if mt > x:
                mt = x
        self.memo[(start, d)] = mt
        return mt
