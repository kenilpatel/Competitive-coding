class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = defaultdict(lambda:[0,0,0,0,0,0,0,0,0,0])
        col = defaultdict(lambda:[0,0,0,0,0,0,0,0,0,0])
        overall = defaultdict(lambda:[0,0,0,0,0,0,0,0,0,0])
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] != '.':
                    dig = int(board[i][j]) 
                    x = 0 
                    y = 0
                    if 0 <= i <= 2:
                        x = 0
                    if 3 <= i <= 5:
                        x = 1
                    if 6 <= i <= 8:
                        x = 2
                        
                    if 0 <= j <= 2:
                        y = 0
                    if 3 <= j <= 5:
                        y = 1
                    if 6 <= j <= 8:
                        y = 2  
                    row[i][dig] += 1
                    col[j][dig] += 1
                    overall[(x,y)][dig] += 1 
        for i in range(n):
            for l in row[i]:
                if l >= 2:
                    return False
        for i in range(n):
            for l in col[i]:
                if l >= 2:
                    return False
        for i in range(3):
            for j in range(3):
                for l in overall[(i,j)]:
                    if l >= 2:
                        return False
        return True
