class Solution(object):
    def get(self):
        return False

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        ps = []
        i = 1
        while i**2 <= n:
            ps.append(i**2)
            i += 1
        ps = ps[::-1]
        # print(ps)
        queue = [(n, 0)]
        visited = defaultdict(self.get)
        visited[n] = True
        while len(queue) != 0:
            top, step = queue[0]
            if top == 0:
                return step
            queue = queue[1:]
            l = []
            for i in ps:
                if top - i >= 0 and visited[top - i] == False:
                    visited[top - i] = True
                    queue.append((top - i, step + 1))
