class Solution(object):
    def get(self):
        return 9999

    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        q = [(0, 0, k, 0)]
        visited = set()
        visited.add((0, 0, k))
        m = len(grid)
        n = len(grid[0])
        while q:
            x, y, k, step = q.pop(0)
            if x == m - 1 and y == n - 1:
                return step
            for mx, my in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y-1)]:
                if mx >= 0 and mx < m and my >= 0 and my < n:
                    if k > 0:
                        if grid[mx][my] == 0 and (mx, my, k) not in visited:
                            visited.add((mx, my, k))
                            q.append((mx, my, k, step + 1))
                        if grid[mx][my] == 1 and (mx, my, k - 1) not in visited:
                            visited.add((mx, my, k - 1))
                            q.append((mx, my, k - 1, step + 1))
                    else:
                        if grid[mx][my] == 0 and (mx, my, k) not in visited:
                            visited.add((mx, my, k))
                            q.append((mx, my, k, step + 1))
        return -1
