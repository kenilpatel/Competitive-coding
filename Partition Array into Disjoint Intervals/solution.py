class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        max_t = []
        n = len(A)
        maxn = 0
        for i in range(n):
            maxn = max(maxn,A[i])
            max_t.append(maxn)
        min_t = [0] * n
        minn = float('inf')
        for i in range(n - 1,-1,-1):
            minn = min(minn,A[i])
            min_t[i] = minn
        for i in range(0,n - 1):
            if max_t[i] <= min_t[i + 1]:
                return i + 1
        
