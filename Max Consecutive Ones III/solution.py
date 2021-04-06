class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if K == 0:
            fa = 0
            ans = 0 
            for i in A:
                if i == 0:
                    fa = max(fa,ans)
                    ans = 0 
                else:
                    ans += i
            fa = max(fa,ans)
            return fa
        n = len(A)
        i = 0 
        sw = 0 
        lk = K
        ans = 0
        for j in range(n):  
            if A[j] == 0:
                if lk == 0:
                    if A[i] == 0:
                        i += 1 
                    else:
                        while A[i] != 0:
                            sw -= 1
                            i += 1
                        i += 1 
                else:
                    sw += 1 
                    lk -= 1
            else:
                sw += 1 
            ans = max(ans,sw) 
        ans = max(ans,sw)
        return ans
