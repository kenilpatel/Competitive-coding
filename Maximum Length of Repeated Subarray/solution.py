class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(A)
        m = len(B)
        mat = [[0] * m for _ in range(n)]
        ans = 0 
        for i in range(n):
            for j in range(m):
                
                if A[i] == B[j]:
                    prev = 0 
                    if i - 1 >= 0 and j - 1 >= 0:
                        prev = mat[i - 1][j - 1]
                    mat[i][j] = 1 + prev
                ans = max(ans,mat[i][j])
        return ans
                    
                    
                
