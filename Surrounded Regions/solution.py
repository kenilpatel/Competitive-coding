import collections


class Solution(object):
    connected = None
    visited = None
    board_g = None

    def getbool(self):
        return False

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        check_index = []
        M = len(board)
        if M == 0:
            return
        N = len(board[0])
        self.connected = defaultdict(self.getbool)
        self.visited = defaultdict(self.getbool)
        self.board_g = board
        for i in range(0, M):
            for j in range(0, N):
                if i == 0 or i == M - 1 or j == 0 or j == N - 1:
                    if board[i][j] == 'O':
                        self.dfs((i, j), M, N)
        for i in range(0, M):
            for j in range(0, N):
                if self.connected[(i, j)] == False:
                    board[i][j] = 'X'

    def dfs(self, tup, M, N):
        self.connected[tup] = True
        if tup[0] < 0 or tup[0] > M - 1 or tup[1] < 0 or tup[1] > N - 1:
            return
        else:
            if self.visited[(tup[0], tup[1] + 1)] == False:
                if tup[1] + 1 <= N - 1 and self.board_g[tup[0]][tup[1] + 1] == 'O':
                    self.visited[(tup[0], tup[1] + 1)] = True
                    self.dfs((tup[0], tup[1] + 1), M, N)
            if self.visited[(tup[0] + 1, tup[1])] == False:
                if tup[0] + 1 <= M - 1 and self.board_g[tup[0] + 1][tup[1]] == 'O':
                    self.visited[(tup[0] + 1, tup[1])] = True
                    self.dfs((tup[0] + 1, tup[1]), M, N)
            if self.visited[(tup[0], tup[1] - 1)] == False:
                if tup[1] - 1 >= 0 and self.board_g[tup[0]][tup[1] - 1] == 'O':
                    self.visited[(tup[0], tup[1] - 1)] = True
                    self.dfs((tup[0], tup[1] - 1), M, N)
            if self.visited[(tup[0] - 1, tup[1])] == False:
                if tup[0] - 1 >= 0 and self.board_g[tup[0] - 1][tup[1]] == 'O':
                    self.visited[(tup[0] - 1, tup[1])] = True
                    self.dfs((tup[0] - 1, tup[1]), M, N)
