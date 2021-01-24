class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix[0])
        for l in matrix:
            if target >= l[0] and target <= l[n - 1]:
                x = bisect.bisect_left(l, target)
                # print(x)
                if l[x] == target:
                    return True
        return False
