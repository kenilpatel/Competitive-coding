class Solution(object):
    def get(self):
        return False

    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        q = [(n, 0)]
        visited = defaultdict(self.get)
        visited[n] = True
        while len(q) != 0:
            c = []
            top, step = q[0]
            q = q[1:]
            if top == 1:
                return step
            if top % 2 == 0:
                c.append(top/2)
            else:
                c.append(top + 1)
                c.append(top - 1)
            for p in c:
                if p == 1:
                    return step + 1
                if visited[p] == False:
                    visited[p] = True
                    q.append((p, step + 1))
