import copy
import collections


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs(board, word, i, j):
                    return True
        return False

    def dfs(self, board, word, i, j):
        if i <= -1 or i >= len(board) or j <= -1 or j >= len(board[0]):
            return False
        if board[i][j] == -1 or board[i][j] != word[0]:
            return False
        if len(word) == 1:
            return True

        temp, board[i][j] = board[i][j], -1
        if self.dfs(board, word[1:], i-1, j):
            return True
        if self.dfs(board, word[1:], i+1, j):
            return True
        if self.dfs(board, word[1:], i, j-1):
            return True
        if self.dfs(board, word[1:], i, j+1):
            return True
        board[i][j] = temp
        return False
