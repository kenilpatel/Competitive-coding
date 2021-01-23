class Solution(object):
    def get(self):
        return []

    def gets(self):
        return ""

    def geti(self):
        return 0

    def getb(self):
        return False

    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        id_i = 1
        source_dict = defaultdict(self.get)
        visited = defaultdict(self.getb)
        island_str = defaultdict(self.gets)
        for i1 in range(0, m):
            for j1 in range(0, n):
                if grid[i1][j1] == 1 and visited[(i1, j1)] == False:
                    visited[(i1, j1)] = True
                    queue = [(i1, j1)]
                    while len(queue) != 0:

                        i, j = queue[0]
                        island_str[id_i] += str(i - i1)
                        island_str[id_i] += str(j - j1)
                        queue = queue[1:]
                        grid[i][j] = id_i
                        if i - 1 >= 0:
                            if grid[i - 1][j] != 0 and visited[(i - 1, j)] == False:
                                visited[(i - 1, j)] = True
                                queue.append((i - 1, j))
                        if i + 1 < m:
                            if grid[i + 1][j] != 0 and visited[(i + 1, j)] == False:
                                visited[(i + 1, j)] = True
                                queue.append((i + 1, j))
                        if j - 1 >= 0:
                            if grid[i][j - 1] != 0 and visited[(i, j - 1)] == False:
                                visited[(i, j - 1)] = True
                                queue.append((i, j - 1))
                        if j + 1 < n:
                            if grid[i][j + 1] != 0 and visited[(i, j + 1)] == False:
                                visited[(i, j + 1)] = True
                                queue.append((i, j + 1))
                    id_i += 1
        uni = defaultdict(self.geti)
        for v in island_str.values():
            uni[v] += 1
        return len(uni.keys())
