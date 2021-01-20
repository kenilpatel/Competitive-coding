class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        match = {'}': '{', ')': '(', "]": "["}
        for p in s:
            if p == "}" or p == ")" or p == "]":
                if len(stack) == 0:
                    return False
                else:
                    top = stack.pop()
                    if top != match[p]:
                        return False
            else:
                stack.append(p)
        if len(stack) == 0:
            return True
        else:
            return False
