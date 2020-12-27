class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if(matrix == []):
            return []
        list_ans = []
        rev = False
        m = len(matrix)
        n = len(matrix[0])
        if m == 1 and n == 0:
            return []
        for i in range(0, m):
            x = i
            y = 0
            list_local = []
            while True:
                list_local.append(matrix[x][y])
                if x - 1 < 0 or y + 1 >= n:
                    break
                x = x - 1
                y = y + 1
            if rev == False:
                list_ans = list_ans + list_local
                rev = True
            else:
                list_local.reverse()
                list_ans = list_ans + list_local
                rev = False
        for i in range(1, n):
            x = m - 1
            y = i
            list_local = []
            while True:
                list_local.append(matrix[x][y])
                if x - 1 < 0 or y + 1 >= n:
                    break
                x = x - 1
                y = y + 1
            if rev == False:
                list_ans = list_ans + list_local
                rev = True
            else:
                list_local.reverse()
                list_ans = list_ans + list_local
                rev = False
        return list_ans
