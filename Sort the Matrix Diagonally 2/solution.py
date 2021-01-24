class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        dig_list1 = []
        dig_list2 = []
        m = len(mat)
        n = len(mat[0])
        for j in range(0, m):
            start_i = j
            start_j = 0
            local = []
            while start_i < m and start_j < n:
                local.append(mat[start_i][start_j])
                start_i = start_i + 1
                start_j = start_j + 1
            dig_list1.append(local)
        for j in range(0, n):
            start_i = 0
            start_j = j
            local = []
            while start_i < m and start_j < n:
                local.append(mat[start_i][start_j])
                start_i = start_i + 1
                start_j = start_j + 1
            dig_list2.append(local)
        for i in range(0, len(dig_list1)):
            dig_list1[i] = sorted(dig_list1[i])
        for i in range(0, len(dig_list2)):
            dig_list2[i] = sorted(dig_list2[i])
        for j in range(0, m):
            start_i = j
            start_j = 0
            ind = j
            for ent in dig_list1[start_i]:
                mat[start_i][start_j] = ent
                start_i = start_i + 1
                start_j = start_j + 1
        for j in range(0, n):
            start_i = 0
            start_j = j
            ind = j
            for ent in dig_list2[start_j]:
                mat[start_i][start_j] = ent
                start_i = start_i + 1
                start_j = start_j + 1
        return mat
