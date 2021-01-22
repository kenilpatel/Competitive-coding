class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        return map(lambda x: [x[0], x[1]], sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)[0:K])
