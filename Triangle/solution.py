class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        row_len = [len(i) for i in triangle]
        for i in range(0,len(triangle)):
            for j in range(0,len(triangle[i])):
                m = i - 1
                n = j
                val1 = float('inf')
                val2 = float('inf')
                if m >= 0:
                    if n < row_len[m]:
                        val1 = triangle[m][n]
                    if n - 1 >= 0:
                        val2 = triangle[m][n - 1]
                    triangle[i][j] += min(val1,val2)
        return min(triangle[-1])
                    
                    
                
