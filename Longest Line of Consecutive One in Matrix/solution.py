class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        m1 = copy.deepcopy(M)
        m2 = copy.deepcopy(M)
        m3 = copy.deepcopy(M)
        m = len(M)
        if m == 0:
            return 0
        n = len(M[0])
        max_n = M[0][0]
        for i in range(1, m):
            for j in range(0, n):
                if i - 1 >= 0 and M[i][j] != 0:
                    M[i][j] = M[i][j] + M[i - 1][j]
                if M[i][j] > max_n:
                    max_n = M[i][j]
        for i in range(0, m):
            for j in range(1, n):
                if j - 1 >= 0 and M[i][j] != 0:
                    m1[i][j] = m1[i][j] + m1[i][j - 1]
                if m1[i][j] > max_n:
                    max_n = m1[i][j]
        for i in range(1, m):
            for j in range(1, n):
                if i - 1 >= 0 and j - 1 >= 0 and M[i][j] != 0:
                    m2[i][j] = m2[i][j] + m2[i - 1][j - 1]
                if m2[i][j] > max_n:
                    max_n = m2[i][j]
        for i in range(1, m):
            for j in range(0, n - 1):
                if i - 1 >= 0 and j + 1 < n and M[i][j] != 0:
                    m3[i][j] = m3[i][j] + m3[i - 1][j + 1]
                if m3[i][j] > max_n:
                    max_n = m3[i][j]
        return max_n
