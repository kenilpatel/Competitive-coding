class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        for char in s:
            if len(stack) == 0:
                stack.append((char, 1))
            else:
                top = stack.pop()
                if top[0] == char:
                    if top[1] + 1 < k:
                        stack.append((char, top[1] + 1))
                else:
                    stack.append(top)
                    stack.append((char, 1))
        ans = ""
        while stack:
            y = stack.pop(0)
            ans += y[0]*y[1]
        return ans
