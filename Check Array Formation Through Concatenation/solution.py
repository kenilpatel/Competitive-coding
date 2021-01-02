class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        ans = False
        length = 0
        for p in pieces:
            x = len(p)
            p_ans = False
            for j in range(0,len(arr) - x + 1):
                # print(p, arr[j:j+x], p == arr[j:j+x])
                if p == arr[j:j+x]:
                    p_ans = True
                    break
            if p_ans == True:
                length = length + x
            else:
                return False
        return True