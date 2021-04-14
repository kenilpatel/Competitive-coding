class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n1 = len(word1)
        n2 = len(word2)
        matrix = [[0 for _ in range(n1)] for _ in range(n2)]
        for i in range(0,n2):
            for j in range(0,n1): 
                if word1[j] == word2[i]:
                    if i - 1 >= 0 and j - 1 >= 0:
                        matrix[i][j] = 1 + matrix[i - 1][j - 1]
                    else:
                        matrix[i][j] = 1
                else:
                    if i - 1 >= 0:
                        matrix[i][j] = matrix[i - 1][j]
                    if j - 1 >= 0:
                        matrix[i][j] = max(matrix[i][j],matrix[i][j - 1])
        return n1 - matrix[n2 - 1][n1 - 1] + n2 - matrix[n2 - 1][n1 - 1]
