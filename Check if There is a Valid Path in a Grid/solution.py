class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """ 
        m = len(grid)
        n = len(grid[0])
        q = []
        i = 0
        j = 0
        if grid[0][0] == 1:
            q.append((i,j,i,j -1))
        elif grid[0][0] == 2:
            q.append((i,j,i - 1,j))
        elif grid[0][0] == 3:
            q.append((i,j,i,j - 1))
        elif grid[0][0] == 4:
            q.append((i,j,i + 1,j))
            q.append((i,j,i,j + 1)) 
        elif grid[0][0] == 6:
            q.append((i,j,i - 1,j))
        visited = set()
        visited.add((i,j))
        while q:
            ci,cj,pi,pj = q.pop(0) 
            # print(ci,cj,pi,pj)
            if 0 <= ci < m and 0 <= cj < n:
                typer = grid[ci][cj]
                if typer == 1: 
                    if pi == ci and pj == cj - 1:
                        if ci == m - 1 and cj == n - 1:
                            return True 
                        if (ci,cj + 1) not in visited:
                            visited.add((ci,cj + 1))
                            q.append((ci,cj + 1,ci,cj))
                    elif pi == ci and pj == cj + 1:
                        if ci == m - 1 and cj == n - 1:
                            return True 
                        if (ci,cj - 1) not in visited:
                            visited.add((ci,cj - 1))
                            q.append((ci,cj - 1,ci,cj)) 
                elif typer == 2:
                    if pi == ci - 1 and pj == cj:
                        if ci == m - 1 and cj == n - 1:
                            return True 
                        if (ci + 1,cj) not in visited:
                            visited.add((ci + 1,cj))
                            q.append((ci + 1,cj,ci,cj))
                    elif pi == ci + 1 and pj == cj:
                        if ci == m - 1 and cj == n - 1:
                            return True 
                        if (ci - 1,cj) not in visited:
                            visited.add((ci - 1,cj))
                            q.append((ci - 1,cj,ci,cj)) 
                elif typer == 3:
                    # print("c,p",ci,cj,pi,pi)
                    if pi == ci and pj == cj - 1:
                        if ci == m - 1 and cj == n - 1:
                            return True 
                        if (ci + 1,cj) not in visited:
                            visited.add((ci + 1,cj))
                            q.append((ci + 1,cj,ci,cj))
                    elif pi == ci + 1 and pj == cj:
                        if ci == m - 1 and cj == n - 1:
                            return True 
                        if (ci,cj - 1) not in visited:
                            visited.add((ci,cj - 1))
                            q.append((ci,cj - 1,ci,cj))
                elif typer == 4:
                    if pi == ci + 1 and pj == cj:
                        if ci == m - 1 and cj == n - 1:
                            return True 
                        if (ci,cj + 1) not in visited:
                            visited.add((ci,cj + 1))
                            q.append((ci,cj + 1,ci,cj))
                    elif pi == ci and pj == cj + 1:
                        if ci == m - 1 and cj == n - 1:
                            return True 
                        if (ci + 1,cj) not in visited:
                            visited.add((ci + 1,cj))
                            q.append((ci + 1,cj,ci,cj))
                elif typer == 5:
                    if pi == ci and pj == cj - 1:
                        if ci == m - 1 and cj == n - 1:
                            return True 
                        if (ci - 1,cj) not in visited:
                            visited.add((ci - 1,cj))
                            q.append((ci - 1,cj,ci,cj))
                    elif pi == ci - 1 and pj == cj:
                        if ci == m - 1 and cj == n - 1:
                            return True 
                        if (ci,cj - 1) not in visited:
                            visited.add((ci,cj - 1))
                            q.append((ci,cj - 1,ci,cj))
                elif typer == 6:
                    if pi == ci - 1 and pj == cj:
                        if ci == m - 1 and cj == n - 1:
                            return True 
                        if (ci,cj + 1) not in visited:
                            visited.add((ci,cj + 1))
                            q.append((ci,cj + 1,ci,cj))
                    elif pi == ci and pj == cj + 1:
                        if ci == m - 1 and cj == n - 1:
                            return True 
                        if (ci - 1,cj) not in visited:
                            visited.add((ci - 1,cj))
                            q.append((ci - 1,cj,ci,cj))
        return False
