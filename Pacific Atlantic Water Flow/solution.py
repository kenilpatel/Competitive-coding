class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        pacific = []
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        pv = set()
        av = set()
        for i in range(0, m):
            start = (i, 0)
            if start not in pv:
                pv.add(start)
                q = [start]
                while q:
                    x, y = q.pop(0)
                    if x + 1 < m:
                        if (x + 1, y) not in pv and matrix[x + 1][y] >= matrix[x][y]:
                            pv.add((x + 1, y))
                            q.append((x + 1, y))
                    if y + 1 < n:
                        if (x, y + 1) not in pv and matrix[x][y + 1] >= matrix[x][y]:
                            pv.add((x, y + 1))
                            q.append((x, y + 1))
                    if x - 1 >= 0:
                        if (x - 1, y) not in pv and matrix[x - 1][y] >= matrix[x][y]:
                            pv.add((x - 1, y))
                            q.append((x - 1, y))
                    if y - 1 >= 0:
                        if (x, y - 1) not in pv and matrix[x][y - 1] >= matrix[x][y]:
                            pv.add((x, y - 1))
                            q.append((x, y - 1))
        for j in range(0, n):
            start = (0, j)
            if start not in pv:
                pv.add(start)
                q = [start]
                while q:
                    x, y = q.pop(0)
                    if x + 1 < m:
                        if (x + 1, y) not in pv and matrix[x + 1][y] >= matrix[x][y]:
                            pv.add((x + 1, y))
                            q.append((x + 1, y))
                    if y + 1 < n:
                        if (x, y + 1) not in pv and matrix[x][y + 1] >= matrix[x][y]:
                            pv.add((x, y + 1))
                            q.append((x, y + 1))
                    if x - 1 >= 0:
                        if (x - 1, y) not in pv and matrix[x - 1][y] >= matrix[x][y]:
                            pv.add((x - 1, y))
                            q.append((x - 1, y))
                    if y - 1 >= 0:
                        if (x, y - 1) not in pv and matrix[x][y - 1] >= matrix[x][y]:
                            pv.add((x, y - 1))
                            q.append((x, y - 1))
        for i in range(0, m):
            start = (i, n - 1)
            if start not in av:
                av.add(start)
                q = [start]
                while q:
                    x, y = q.pop(0)
                    if x + 1 < m:
                        if (x + 1, y) not in av and matrix[x + 1][y] >= matrix[x][y]:
                            av.add((x + 1, y))
                            q.append((x + 1, y))
                    if y + 1 < n:
                        if (x, y + 1) not in av and matrix[x][y + 1] >= matrix[x][y]:
                            av.add((x, y + 1))
                            q.append((x, y + 1))
                    if x - 1 >= 0:
                        if (x - 1, y) not in av and matrix[x - 1][y] >= matrix[x][y]:
                            av.add((x - 1, y))
                            q.append((x - 1, y))
                    if y - 1 >= 0:
                        if (x, y - 1) not in av and matrix[x][y - 1] >= matrix[x][y]:
                            av.add((x, y - 1))
                            q.append((x, y - 1))
        for j in range(0, n):
            start = (m - 1, j)
            if start not in av:
                av.add(start)
                q = [start]
                while q:
                    x, y = q.pop(0)
                    if x + 1 < m:
                        if (x + 1, y) not in av and matrix[x + 1][y] >= matrix[x][y]:
                            av.add((x + 1, y))
                            q.append((x + 1, y))
                    if y + 1 < n:
                        if (x, y + 1) not in av and matrix[x][y + 1] >= matrix[x][y]:
                            av.add((x, y + 1))
                            q.append((x, y + 1))
                    if x - 1 >= 0:
                        if (x - 1, y) not in av and matrix[x - 1][y] >= matrix[x][y]:
                            av.add((x - 1, y))
                            q.append((x - 1, y))
                    if y - 1 >= 0:
                        if (x, y - 1) not in av and matrix[x][y - 1] >= matrix[x][y]:
                            av.add((x, y - 1))
                            q.append((x, y - 1))
        return av.intersection(pv)
