import re


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = re.sub('//+', '/', path)
        commands = path.split('/')
        stack = []
        for cmd in commands:
            if cmd == ".":
                pass
            elif cmd == "..":
                if stack:
                    stack.pop()
            elif cmd != "":
                stack.append(cmd)
        ans = "/"
        sl = len(stack)
        for i in range(0, sl - 1):
            ans += stack[i] + '/'
        if sl >= 1:
            ans += stack[sl - 1]
        return ans
