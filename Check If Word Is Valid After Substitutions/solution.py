import re
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while True:
            new = re.sub("abc","",s)
            if new == s:
                return False
            if new == "":
                return True
            s = new



