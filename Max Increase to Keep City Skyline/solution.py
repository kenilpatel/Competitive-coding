class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_m = defaultdict(lambda: -1)
        col_m = defaultdict(lambda: -1)
        m = len(grid)
        n = len(grid[0])
        for i in range(0, m):
            for j in range(0, n):
                row_m[i] = max(row_m[i], grid[i][j])
                col_m[j] = max(col_m[j], grid[i][j])
        sumn = 0
        for i in range(0, m):
            for j in range(0, n):
                new_h = min(row_m[i], col_m[j])
                sumn += new_h - grid[i][j]
                grid[i][j] = new_h

        return sumn
