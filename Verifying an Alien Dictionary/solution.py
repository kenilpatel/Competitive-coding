class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """ 
        rank = {}
        n = 1
        for i,ele in enumerate(order):
            rank[ele] = n
            n += 1
        def comp(x,y):
            lenx = len(x)
            leny = len(y)
            for i in range(0,min(lenx,leny)):
                if rank[x[i]] < rank[y[i]]:
                    return -1
                elif rank[x[i]] > rank[y[i]]:
                    return 1
            if lenx > leny:
                return 1
            elif lenx < leny:
                return -1
            else:
                return 0
        s_words = sorted(words,cmp = comp) 
        return s_words == words
