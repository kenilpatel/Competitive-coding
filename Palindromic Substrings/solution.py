class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # odd length substrings 
        n = len(s)
        cnt = 0
        for i in range(0,n):
            l = i - 1
            m = i + 1
            cnt += 1
            while l >= 0 and m < n and s[l] == s[m]:
                cnt += 1
                l -= 1
                m += 1
        for i in range(0,n - 1):
            l = i
            m = i + 1
            while l >= 0 and m < n and s[l] == s[m]:
                cnt += 1
                l -= 1
                m += 1
        return cnt
                
        
