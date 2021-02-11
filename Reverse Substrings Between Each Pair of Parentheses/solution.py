class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in s:
            if i == ')':
                rev = ""
                while True:
                    top = stack.pop()
                    if top == "(":
                        break
                    else:
                        rev += top
                for j in rev:
                    stack.append(j)
            else:
                stack.append(i)
        return "".join(stack)
