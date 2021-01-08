class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        prevset = ["a", "b", "c"]
        curset = ["ab", "ac", "ba", "bc", "ca", "cb"]
        curk = 0
        for i in prevset:
            if len(i) == n:
                curk = curk + 1
            if curk == k:
                return i
        for i in curset:
            if len(i) == n:
                curk = curk + 1
            if curk == k:
                return i
        while True:
            new_set = []
            for i in prevset:
                for j in curset:
                    if i[len(i) - 1] != j[0]:
                        if len(i + j) > n:
                            break
                        if len(i + j) == n:
                            curk = curk + 1
                        if curk == k:
                            return i + j
                        else:
                            new_set.append(i + j)
            curset = new_set
            if len(curset) == 0:
                return ""
        return ""
