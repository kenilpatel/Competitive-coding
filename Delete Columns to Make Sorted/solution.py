class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """ 
        n = len(strs)
        m = len(strs[0])  
        ans = 0
        for j in range(m): 
            for i in range(1,n):
                if strs[i][j] >= strs[i - 1][j]:
                    continue
                else:
                    ans += 1
                    break
        return ans
