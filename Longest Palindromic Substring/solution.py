class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        best = 0
        ans = ""
        for i in range(0, size):
            if best == 0:
                ans = s[i]
                best = 1
            fp = i - 1
            sp = i + 1
            # print(i,s[i])
            while fp >= 0 and sp < size and s[fp] == s[sp]:
                # print(s[fp:sp + 1])
                if best < sp - fp:
                    best = sp - fp
                    ans = s[fp:sp + 1]
                fp -= 1
                sp += 1

        for i in range(0, size - 1):
            if s[i] == s[i + 1]:
                if best == 0 or best == 1:
                    ans = s[i] + s[i + 1]
                    best = 2
                fp = i - 1
                sp = i + 2
                while fp >= 0 and sp < size and s[fp] == s[sp]:
                    if best < sp - fp:
                        best = sp - fp
                        ans = s[fp:sp + 1]
                    fp -= 1
                    sp += 1
        return ans
