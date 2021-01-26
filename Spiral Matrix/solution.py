class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        return self.get_boarder(matrix)

    def get_boarder(self, matrix):
        if matrix == []:
            return []
        if len(matrix) == 0:
            if len(matrix[0]) == 0:
                return []
        else:
            if len(matrix) == 1:
                return matrix[0]
            else:
                new_matrix = []
                x1 = matrix[0]
                x2 = matrix[len(matrix) - 1]
                a1 = []
                a2 = []
                for i in range(1, len(matrix) - 1):
                    l = copy.deepcopy(matrix[i])
                    new_matrix.append(copy.deepcopy(l[1:len(l) - 1]))
                    if len(l) >= 1:
                        a1.append(l[len(l) - 1])
                        l = l[0:len(l) - 1]
                    if len(l) >= 1:
                        a2.append(l[0])
                return x1 + a1 + x2[::-1] + a2[::-1] + self.get_boarder(new_matrix)
