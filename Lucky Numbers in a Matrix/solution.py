import numpy


class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        return list(set([min(x) for x in matrix]).intersection(set([max(x) for x in numpy.transpose(matrix)])))
