class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        for i in range(0, len(S)):
            if not stack:
                stack.append(S[i])
            else:
                top = stack.pop()
                if S[i] == top:
                    continue
                else:
                    stack.append(top)
                    stack.append(S[i])
        return "".join(stack)
