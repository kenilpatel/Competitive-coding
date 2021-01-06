class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in range(0, len(matrix[0])):
            if target >= matrix[0][i] and target <= matrix[len(matrix) - 1][i]:
                index = i
                low = 0
                high = len(matrix) - 1
                while True:
                    mid = int(high + low) / 2
                    if high < low:
                        break
                    if matrix[mid][i] == target:
                        return True
                    if matrix[mid][i] < target:
                        low = mid + 1
                    else:
                        high = mid - 1
        return False
