class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        fresh = 0
        rot = []
        m = len(grid)
        n = len(grid[0])
        time = 0
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rot.append([i, j, time])
        while (len(rot)) != 0:
            i, j, time = rot[0]
            rot = rot[1:]
            if i-1 >= 0:
                if grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    rot.append([i-1, j, time + 1])
                    fresh -= 1
            if j-1 >= 0:
                if grid[i][j - 1] == 1:
                    grid[i][j - 1] = 2
                    rot.append([i, j - 1, time + 1])
                    fresh -= 1
            if i+1 < m:
                if grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    rot.append([i+1, j, time + 1])
                    fresh -= 1
            if j+1 < n:
                if grid[i][j + 1] == 1:
                    grid[i][j + 1] = 2
                    rot.append([i, j + 1, time + 1])
                    fresh -= 1
        if fresh == 0:
            return time
        else:
            return -1
