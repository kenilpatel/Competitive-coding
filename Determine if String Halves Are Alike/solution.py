class Solution(object):
    def get(self):
        return 0

    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        left = s[0:len(s)/2]
        right = s[len(s)/2:]
        print(left, right)
        d1 = 0
        d2 = 0
        x = ['a', 'e', 'i', 'o', 'u']
        for i in left:
            if i in x:
                d1 += 1
        for i in right:
            if i in x:
                d2 += 1
        if d1 != d2:
            return False
        return True
