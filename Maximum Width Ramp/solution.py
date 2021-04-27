class Solution(object):
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ia = []
        for i,ele in enumerate(A):
            ia.append((ele,i))
        ia = sorted(ia)
        # print(ia)
        idx = ia[0][1]
        n = len(A)
        ans = 0
        for i in range(1,n):
            if ia[i][1] < idx:
                idx = ia[i][1]
            else:
                ans = max(ans,ia[i][1] - idx)
        return ans
            
