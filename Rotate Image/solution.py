class Solution(object):
    def get(self):
        return False

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        start = 0
        end = len(matrix)
        while start < end:
            f1 = []
            i = start
            visited = defaultdict(self.get)
            for j in range(start, end):
                f1.append(matrix[i][j])
            i = end - 1
            f3 = []
            for j in range(end - 1, start - 1, -1):
                f3.append(matrix[i][j])
            f2 = []
            j = end - 1
            for i in range(start, end):
                f2.append(matrix[i][j])
            f4 = []
            j = start
            for i in range(end - 1, start - 1, -1):
                f4.append(matrix[i][j])
            for j in range(start, end):
                matrix[i][j] = f4.pop(0)
            for i in range(start, end):
                matrix[i][j] = f1.pop(0)
            for j in range(end - 1, start - 1, -1):
                matrix[i][j] = f2.pop(0)
            for i in range(end - 1, start - 1, -1):
                matrix[i][j] = f3.pop(0)
            start += 1
            end -= 1
