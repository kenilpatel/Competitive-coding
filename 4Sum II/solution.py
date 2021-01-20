class Solution(object):
    def get(self):
        return 0
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        N = len(A)
        D = sorted(D)
        sum1 = defaultdict(self.get)
        for i in C:
            for j in D:
                sum1[-(i + j)] += 1
        cnt = 0
        for i in A:
            for j in B:
                cnt += sum1[i + j]
        return cnt