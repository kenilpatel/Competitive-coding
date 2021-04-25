class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        arr = []
        for i in range(lo,hi + 1):
            step = 0 
            num = i 
            while num != 1: 
                if num % 2 == 0:
                    num = num / 2
                else:
                    num = 3 * num + 1 
                step += 1
            arr.append((step,i))
        arr = sorted(arr)
        return arr[k - 1][1]
