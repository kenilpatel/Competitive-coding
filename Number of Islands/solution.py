class Solution(object):
    def get(self):
        return False

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        no = 0
        visited = defaultdict(self.get)
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == "1" and visited[(i, j)] == False:
                    no = no + 1
                    grid[i][j] = no
                    visited[(i, j)] = True
                    q = [(i, j)]
                    v = defaultdict(self.get)
                    while len(q) != 0:
                        x, y = q[0]
                        # print("top",x,y)
                        q = q[1:]
                        if x + 1 < m:
                            if grid[x+1][y] == "1":
                                if visited[(x+1, y)] == False and v[(x+1, y)] == False:
                                    visited[(x+1, y)] = True
                                    v[(x+1, y)] = True
                                    q.append((x+1, y))
                                    grid[x+1][y] = no
                        if y + 1 < n:
                            if grid[x][y+1] == "1":
                                if visited[(x, y+1)] == False and v[(x, y+1)] == False:
                                    visited[(x, y+1)] = True
                                    v[(x, y+1)] = True
                                    q.append((x, y+1))
                                    grid[x][y+1] = no
                        if x - 1 >= 0:
                            if grid[x-1][y] == "1":
                                if visited[(x-1, y)] == False and v[(x-1, y)] == False:
                                    visited[(x-1, y)] = True
                                    v[(x-1, y)] = True
                                    q.append((x-1, y))
                                    grid[x-1][y] = no
                        if y - 1 >= 0:
                            if grid[x][y-1] == "1":
                                if visited[(x, y-1)] == False and v[(x, y-1)] == False:
                                    visited[(x, y-1)] = True
                                    v[(x, y-1)] = True
                                    q.append((x, y-1))
                                    grid[x][y-1] = no
        # print(grid)
        return no
