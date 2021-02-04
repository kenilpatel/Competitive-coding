class Solution(object):
    def get(self):
        return set()

    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        ntoc = {}
        cton = {}
        moves = defaultdict(self.get)
        number = n * n
        check = n % 2
        if board[0][0] != -1:
            return -1
        if check == 0:
            check = 1
        else:
            check = 0
        for i in range(0, n):
            l = []
            for j in range(0, n):
                l.append(number)
                number -= 1
            if i % 2 == check:
                l = l[::-1]
            for j in range(0, n):
                popno = l.pop(0)
                ntoc[popno] = (i, j)
                cton[(i, j)] = popno
        for i in range(0, n):
            for j in range(0, n):
                place = cton[(i, j)]
                for dice in range(1, 7):
                    new_place = place + dice
                    # print("new",new_place)
                    if new_place <= n*n:
                        x, y = ntoc[new_place]
                        if board[x][y] == -1:
                            moves[place].add(new_place)
                        else:
                            moves[place].add(board[x][y])
        q = [(1, 0)]
        visited = set()
        visited.add((1, 0))
        target = n * n
        while q:
            top, step = q.pop(0)
            if top == target:
                return step
            for c in moves[top]:
                if (c, step + 1) not in visited:
                    visited.add((c, step + 1))
                    q.append((c, step + 1))
