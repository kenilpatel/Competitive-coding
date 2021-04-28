class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        row_sum = copy.deepcopy(grid)
        col_sum = copy.deepcopy(grid)
        m = len(grid)
        n = len(grid[0])
        for i in range(0,m):
            for j in range(0,n):  
                if j - 1 >= 0:
                    row_sum[i][j] += row_sum[i][j - 1]
                    
        for j in range(0,n):
            for i in range(0,m):
                if i - 1 >= 0:
                    col_sum[i][j] += col_sum[i - 1][j]
        
        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j] == 1:
                    ans = max(ans,1)
                row = i - 1
                col = j - 1
                for size in range(1,min(m,n)):
                    end_row = i + size
                    end_col = j + size
                    one = 0 
                    two = 0 
                    three = 0
                    four = 0
                    if end_row < m and end_col < n:
                        one = row_sum[i][end_col] 
                        two = row_sum[end_row][end_col]
                        if col >= 0:
                            one -= row_sum[i][col]
                            two -= row_sum[end_row][col]
                        three = col_sum[end_row][j] 
                        four = col_sum[end_row][end_col]
                        if row >= 0:
                            four -= col_sum[row][end_col]
                            three -= col_sum[row][j]
                        if one == two == three == four and one == size + 1: 
                            ans = max(ans,(size + 1) ** 2)
                    else:
                        break
        return ans
