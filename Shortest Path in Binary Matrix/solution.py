class Solution(object):
    def getb(self):
        return False

    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        start = (0, 0)
        N = len(grid) - 1
        target = (N, N)
        print(target)
        q = []
        if grid[0][0] == 0:
            q.append((start, 1))
            visited = defaultdict(self.getb)
            visited[start] = True
        while len(q) != 0:
            start, step = q[0]
            if start == target:
                return step
            i = start[0]
            j = start[1]
            q = q[1:]
            move = []
            if i - 1 >= 0:
                if grid[i-1][j] == 0:
                    move.append(((i - 1, j), step + 1))
            if j - 1 >= 0:
                if grid[i][j-1] == 0:
                    move.append(((i, j - 1), step + 1))
            if i + 1 <= N:
                if grid[i+1][j] == 0:
                    move.append(((i + 1, j), step + 1))
            if j + 1 <= N:
                if grid[i][j+1] == 0:
                    move.append(((i, j+1), step + 1))
            if i + 1 <= N and j + 1 <= N:
                if grid[i+1][j+1] == 0:
                    move.append(((i+1, j+1), step + 1))
            if i - 1 >= 0 and j - 1 >= 0:
                if grid[i-1][j-1] == 0:
                    move.append(((i-1, j-1), step + 1))
            if i-1 >= 0 and j+1 <= N:
                if grid[i-1][j+1] == 0:
                    move.append(((i-1, j+1), step + 1))
            if i+1 <= N and j-1 >= 0:
                if grid[i+1][j-1] == 0:
                    move.append(((i+1, j-1), step+1))
            for m in move:
                if m[0] == target:
                    return m[1]
                if visited[m[0]] == False:
                    visited[m[0]] = True
                    q.append(m)
        return -1
