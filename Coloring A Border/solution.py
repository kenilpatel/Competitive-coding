class Solution(object):
    def colorBorder(self, grid, r0, c0, color):
        """
        :type grid: List[List[int]]
        :type r0: int
        :type c0: int
        :type color: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        q = [(r0,c0)]
        gc = grid[r0][c0]
        visited = set() 
        visited.add(q[0])
        move = lambda x,y:[(x + 1,y),(x - 1,y),(x,y + 1),(x,y - 1)]
        check = set()
        while q:
            top = q.pop(0) 
            nc = 0
            for x,y in move(top[0],top[1]): 
                if x <= m - 1 and y <= n - 1 and x >= 0 and y >= 0 and (x,y) not in visited:
                    if grid[x][y] == gc:
                        q.append((x,y))
                        visited.add((x,y)) 
                    else:
                        nc += 1 
            if top[0] == 0 or top[0] == m - 1 or top[1] == 0 or top[1] == n - 1 or nc != 0:
                check.add(top) 
        for x,y in check:
            grid[x][y] = color
        return grid
                    
            
