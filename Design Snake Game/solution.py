class SnakeGame(object):
    f = None
    m = None
    n = None
    head = None
    findex = None
    snack = None

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.snack = [[0, 0]]
        self.head = [0, 0]
        self.f = food
        self.m = height - 1
        self.n = width - 1
        self.findex = 0

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        # print(direction,self.snack)
        i = self.head[0]
        j = self.head[1]
        direction = direction[0]
        if direction == 'U':
            if i-1 >= 0:
                move = [i-1, j]
                if move in self.snack[1:]:
                    return -1
                else:
                    if self.findex < len(self.f):
                        if move == self.f[self.findex]:
                            self.snack.append(move)
                            self.findex += 1
                            self.head = move
                            return len(self.snack) - 1
                        else:
                            self.snack = self.snack[1:]
                            self.snack.append(move)
                            self.head = move
                            return len(self.snack) - 1
                    else:
                        self.snack = self.snack[1:]
                        self.snack.append(move)
                        self.head = move
                        return len(self.snack) - 1
            else:
                return -1
        if direction == 'D':
            if i + 1 <= self.m:
                move = [i+1, j]
                if move in self.snack[1:]:
                    return -1
                else:
                    if self.findex < len(self.f):
                        if move == self.f[self.findex]:
                            self.snack.append(move)
                            self.findex += 1
                            self.head = move
                            return len(self.snack) - 1
                        else:
                            self.snack = self.snack[1:]
                            self.snack.append(move)
                            self.head = move
                            return len(self.snack) - 1
                    else:
                        self.snack = self.snack[1:]
                        self.snack.append(move)
                        self.head = move
                        return len(self.snack) - 1
            else:
                return -1
        if direction == 'R':
            if j+1 <= self.n:
                move = [i, j+1]
                if move in self.snack[1:]:
                    return -1
                else:
                    if self.findex < len(self.f):
                        if move == self.f[self.findex]:
                            self.snack.append(move)
                            self.findex += 1
                            self.head = move
                            return len(self.snack) - 1
                        else:
                            self.snack = self.snack[1:]
                            self.snack.append(move)
                            self.head = move
                            return len(self.snack) - 1
                    else:
                        self.snack = self.snack[1:]
                        self.snack.append(move)
                        self.head = move
                        return len(self.snack) - 1
            else:
                return -1
        if direction == 'L':
            if j-1 >= 0:
                move = [i, j-1]
                if move in self.snack[1:]:
                    return -1
                else:
                    if self.findex < len(self.f):
                        if move == self.f[self.findex]:
                            self.snack.append(move)
                            self.findex += 1
                            self.head = move
                            return len(self.snack) - 1
                        else:
                            self.snack = self.snack[1:]
                            self.snack.append(move)
                            self.head = move
                            return len(self.snack) - 1
                    else:
                        self.snack = self.snack[1:]
                        self.snack.append(move)
                        self.head = move
                        return len(self.snack) - 1
            else:
                return -1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
