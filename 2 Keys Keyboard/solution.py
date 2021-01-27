class Solution(object):
    def getb(self):
        return False

    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        q = [(1, 0, 0)]
        visited = defaultdict(self.getb)
        visited[(1, 0)] = True
        while len(q) != 0:
            top, paste, step = q[0]
            q = q[1:]
            if top == n:
                return step
            if paste != 0 and top + paste <= n and visited[(top + paste, paste)] == False:
                visited[(top + paste, paste)] = True
                if top + paste == n:
                    return step + 1
                q.append((top + paste, paste, step + 1))
            if top > paste and visited[(top, top)] == False:
                visited[(top, top)] = True
                q.append((top, top, step + 1))
