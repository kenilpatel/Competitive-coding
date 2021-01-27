class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        invalid = []
        for i in range(0, len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                match = -1
                while len(stack) > 0:
                    top = stack.pop()
                    if s[top] == '(':
                        match = top
                        break
                if match == -1:
                    invalid.append(i)
        invalid = invalid + stack
        s = list(s)
        for i in invalid:
            s[i] = ""
        return "".join(s)
