class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0]) 
        for i in range(0,m):
            for j in range(0,n):
                q = [(i,j,0)]
                visited = set()
                visited.add((i,j))
                while q:
                    x,y,step = q.pop(0)
                    if matrix[x][y] == 0:
                        break
                    next_s = [(x + 1,y),(x,y + 1),(x - 1,y),(x,y - 1)]
                    for nx,ny in next_s:
                        if 0 <= nx < m and 0 <= ny < n and (nx,ny) not in visited:
                            visited.add((nx,ny))
                            q.append((nx,ny,step + 1))
                matrix[i][j] = step
        return matrix
        
