class Solution(object):
    ans = None

    def getzero(self):
        return 0

    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        self.length = []
        self.ans = []
        self.getpartition(S)
        return self.ans

    def getpartition(self, S):
        left = defaultdict(self.getzero)
        rest = defaultdict(self.getzero)
        for i in range(0, len(S)):
            rest[S[i]] += 1
        for i in range(0, len(S)):
            left[S[i]] += 1
            rest[S[i]] -= 1
            if self.isposible(left, rest):
                self.ans.append(i + 1 - 0)
                self.getpartition(S[i + 1:])
                return

    def isposible(self, left, rest):
        for key in left.keys():
            if rest[key] != 0:
                return False
        return True
