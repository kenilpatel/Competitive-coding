class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        old = {}
        N = len(board)
        M = len(board[0])
        for i in range(0, N):
            for j in range(0, M):
                sum_cell = 0
                if i + 1 <= N - 1 and j + 1 <= M - 1:
                    if (i + 1, j + 1) in old.keys():
                        sum_cell = sum_cell + old[(i + 1, j + 1)]
                    else:
                        sum_cell = sum_cell + board[i + 1][j + 1]
                if i - 1 >= 0 and j + 1 <= M - 1:
                    if (i - 1, j + 1) in old.keys():
                        sum_cell = sum_cell + old[(i - 1, j + 1)]
                    else:
                        sum_cell = sum_cell + board[i - 1][j + 1]
                if j + 1 <= M - 1:
                    if (i, j + 1) in old.keys():
                        sum_cell = sum_cell + old[(i, j + 1)]
                    else:
                        sum_cell = sum_cell + board[i][j + 1]
                if i + 1 <= N - 1:
                    if (i + 1, j) in old.keys():
                        sum_cell = sum_cell + old[(i + 1, j)]
                    else:
                        sum_cell = sum_cell + board[i + 1][j]
                if i - 1 >= 0:
                    if (i - 1, j) in old.keys():
                        sum_cell = sum_cell + old[(i - 1, j)]
                    else:
                        sum_cell = sum_cell + board[i - 1][j]
                if i - 1 >= 0 and j - 1 >= 0:
                    if (i - 1, j - 1) in old.keys():
                        sum_cell = sum_cell + old[(i - 1, j - 1)]
                    else:
                        sum_cell = sum_cell + board[i - 1][j - 1]
                if j - 1 >= 0:
                    if (i, j - 1) in old.keys():
                        sum_cell = sum_cell + old[(i, j - 1)]
                    else:
                        sum_cell = sum_cell + board[i][j - 1]
                if i + 1 <= N - 1 and j - 1 >= 0:
                    if (i + 1, j - 1) in old.keys():
                        sum_cell = sum_cell + old[(i + 1, j - 1)]
                    else:
                        sum_cell = sum_cell + board[i + 1][j - 1]
                old_val = board[i][j]
                if sum_cell < 2:
                    new = 0
                elif sum_cell == 2 or sum_cell == 3:
                    if sum_cell == 3:
                        new = 1
                    else:
                        new = old_val
                if sum_cell > 3:
                    new = 0
                if old_val != new:
                    board[i][j] = new
                    old[(i, j)] = old_val
