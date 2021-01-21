class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        max_l = 0
        for i in range(0, m):
            for j in range(0, n):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] == 1:
                    max_l = 1
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != 0:
                    matrix[i][j] = matrix[i][j] + \
                        min(matrix[i][j - 1], matrix[i - 1]
                            [j], matrix[i - 1][j - 1])
                if matrix[i][j] > max_l:
                    max_l = matrix[i][j]
        return max_l * max_l
