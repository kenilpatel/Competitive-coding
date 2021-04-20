class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        ans = []
        A = sorted(A)
        n = len(A)
        for i in range(n):
            find = B[i] 
            idx = bisect.bisect_left(A,find) 
            while idx < n and A[idx] == find: 
                idx += 1
            if idx >= n:
                n -= 1
                ans.append(A[0])
                A = A[1:]
            else:
                n -= 1
                ans.append(A[idx])
                A = A[0:idx] + A[idx + 1:]    
                
        return ans
            
                
                
                
