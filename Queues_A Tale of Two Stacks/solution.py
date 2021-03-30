class MyQueue(object):
    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.l1 = 0
        self.l2 = 0

    def peek(self):
        if self.l2 > 0:
            return self.s2[self.l2 - 1]
        else:
            while self.s1:
                self.s2.append(self.s1.pop())
                self.l2 += 1
                self.l1 -= 1
            return self.s2[self.l2 - 1]

    def pop(self):
        if self.l2 > 0:
            self.l2 -= 1
            return self.s2.pop()
        else:
            while self.s1:
                self.s2.append(self.s1.pop())
                self.l2 += 1
                self.l1 -= 1
            self.l2 -= 1
            return self.s2.pop()

    def put(self, value):
        self.s1.append(value)
        self.l1 += 1

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())