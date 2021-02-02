class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        wd = []
        ans = []
        for i in range(len(T) - 1, -1, -1):
            top = None
            while stack:
                top = stack.pop()
                if top[0] > T[i]:
                    break
            if top == None:
                pass
            elif top[0] > T[i]:
                ans.append(top[1] - i)
            else:
                ans.append(0)
            if top != None:
                if top[0] > T[i]:
                    stack.append(top)
            else:
                ans.append(0)
            stack.append((T[i], i))
        return ans[::-1]
