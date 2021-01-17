import copy


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        matrix = []
        size = len(s)
        if numRows == 1:
            return s
        for i in range(numRows):
            matrix.append(["0"]*size)
        matrix
        i = 0
        j = 0
        typ = 0
        for char in s:
            matrix[i][j] = char
            if typ == 0:
                i = i + 1
                if i == numRows - 1:
                    typ = 1
            elif typ == 1:
                i = i - 1
                j = j + 1
                if i == 0:
                    typ = 0
        ans = ""
        noc = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                ans += matrix[i][j] if matrix[i][j] != "0" else ""
                noc += 1 if matrix[i][j] != "0" else 0
                if noc >= size:
                    break
        return ans
