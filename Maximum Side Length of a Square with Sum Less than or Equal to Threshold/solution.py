class Solution(object): 
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """ 
        m = len(mat)
        n = len(mat[0])
        rs = copy.deepcopy(mat) 
        for i in range(0,m):
            for j in range(1,n):
                rs[i][j] += rs[i][j - 1]  
                
        def check(size):
            if size == 0:
                return True
            for i in range(0,m - size + 1):
                for j in range(0,n - size + 1):
                    sumn = 0  
                    for k in range(i,i + size): 
                        sumn += rs[k][j + size - 1]
                        if j - 1 >= 0:
                            sumn -= rs[k][j - 1] 
                        if sumn > threshold:
                            break
                    if sumn <= threshold:
                        return True
            return False
        
        lo = 0 
        hi = min(m,n)
        ans = 0 
        while lo <= hi: 
            mid = int((lo + hi) / 2) 
            if check(mid):
                ans = max(ans,mid)
                lo = mid + 1
            else:
                hi = mid - 1
        return ans     
                
