class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        max_c = 0
        visited = set()
        for i in range(0, m):
            for j in range(0, n):
                if (i, j) not in visited and grid[i][j] == 1:
                    q = [(i, j)]
                    conn = 0
                    visited.add((i, j))
                    while len(q) != 0:
                        conn += 1
                        x, y = q[0]
                        q = q[1:]
                        if x + 1 < m:
                            if (x + 1, y) not in visited and grid[x + 1][y] == 1:
                                visited.add((x + 1, y))
                                q.append((x + 1, y))
                        if y + 1 < n:
                            if (x, y + 1) not in visited and grid[x][y + 1] == 1:
                                visited.add((x, y + 1))
                                q.append((x, y + 1))
                        if x - 1 >= 0:
                            if (x - 1, y) not in visited and grid[x - 1][y] == 1:
                                visited.add((x - 1, y))
                                q.append((x - 1, y))
                        if y - 1 >= 0:
                            if (x, y - 1) not in visited and grid[x][y - 1] == 1:
                                visited.add((x, y - 1))
                                q.append((x, y - 1))
                    if max_c < conn:
                        max_c = conn
        return max_c
