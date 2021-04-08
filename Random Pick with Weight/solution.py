from random import randrange
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w
        self.w.insert(0,0)
        n = len(self.w)
        for i in range(1,n):
            self.w[i] += self.w[i - 1] 
        self.n = self.w[n - 1]
    def pickIndex(self):
        """
        :rtype: int
        """
        idx = bisect.bisect_right(self.w,randrange(self.n))
        return idx - 1

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
