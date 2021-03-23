class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        gc = 0 
        lc = 0
        for i,ele in enumerate(A):
            if ele - i != 0:
                diff = abs(ele - i)
                if diff == 1:
                    if i + 1 < n:
                        if A[i] > A[i + 1]:
                            lc += 1
                        else:
                            gc += diff
                    else:
                        gc += diff
                else:
                    gc += diff
        return lc == gc
