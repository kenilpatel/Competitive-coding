class Solution(object):
    start_dict = None
    m = None
    n = None

    def getl(self):
        return []

    def getb(self):
        return False

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.m = len(board)
        self.n = len(board[0])
        # used = copy.deepcopy(board)
        self.start_dict = defaultdict(self.getl)
        for i in range(0, self.m):
            for j in range(0, self.n):
                self.start_dict[board[i][j]].append((i, j))
        ans = []
        for w in words:
            x = len(w) - 1
            if self.search(board, w, x) == True:
                ans.append(w)
            else:
                if self.search(board, w[::-1], x) == True:
                    ans.append(w)
        return ans

    def search(self, board, word, limit):
        for tup in self.start_dict[word[0]]:
            queue = [(tup[0], tup[1], 0)]
            visited = defaultdict(self.getb)
            visited[(tup[0], tup[1])] = True
            while len(queue) != 0:
                i, j, index = queue[0]
                if index == limit:
                    return True
                queue = queue[1:]
                if i - 1 >= 0:
                    if board[i - 1][j] == word[index + 1] and visited[(i - 1, j)] == False:
                        visited[(i - 1, j)] = True
                        queue.append((i - 1, j, index + 1))
                if i + 1 < self.m:
                    if board[i + 1][j] == word[index + 1] and visited[(i + 1, j)] == False:
                        visited[(i + 1, j)] = True
                        queue.append((i + 1, j, index + 1))
                if j - 1 >= 0:
                    if board[i][j - 1] == word[index + 1] and visited[(i, j - 1)] == False:
                        visited[(i, j - 1)] = True
                        queue.append((i, j - 1, index + 1))
                if j + 1 < self.n:
                    if board[i][j + 1] == word[index + 1] and visited[(i, j + 1)] == False:
                        visited[(i, j + 1)] = True
                        queue.append((i, j + 1, index + 1))
        return False
