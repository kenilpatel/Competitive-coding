class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        start = (0, 0)
        N = len(grid)
        end = (N-1, N-1)
        fringe = [(start, grid[start[0]][start[1]])]
        expanded = []
        t = 0
        while len(fringe) != 0:
            top, time = fringe[0]
            t = t if t > time else time
            if top == end:
                return t
            fringe = fringe[1:]
            expanded = expanded + [top]
            i = top[0]
            j = top[1]
            if i - 1 >= 0 and (i-1, j) not in expanded:
                fringe = fringe + [((i-1, j), grid[i-1][j])]
            if i + 1 < N and (i+1, j) not in expanded:
                fringe = fringe + [((i+1, j), grid[i+1][j])]
            if j - 1 >= 0 and (i, j-1) not in expanded:
                fringe = fringe + [((i, j-1), grid[i][j-1])]
            if j + 1 < N and (i, j+1) not in expanded:
                fringe = fringe + [((i, j+1), grid[i][j+1])]
            fringe.sort(key=lambda x: x[1])
