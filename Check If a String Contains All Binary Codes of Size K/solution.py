class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        n = len(s) - k 
        bset = set()
        i = 0
        while i <= n:
            try: 
                bs = s[i:i + k]
                bset.add(bs)
                i += 1  
            except: 
                return False 
        return len(bset) == 2 ** k
