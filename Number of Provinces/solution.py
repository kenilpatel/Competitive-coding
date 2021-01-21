class Solution(object):
    def get(self):
        return []

    def getb(self):
        return False

    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        connection = defaultdict(self.get)
        explored = defaultdict(self.getb)
        for i in range(0, n):
            for j in range(0, n):
                if i != j and isConnected[i][j] == 1:
                    connection[i + 1].append(j + 1)
        region = 0
        # print(connection)
        for i in range(0, n):
            if explored[i + 1] == False:
                # print("exploring",i+1)
                region += 1
                queue = [i + 1]
                visited = defaultdict(self.getb)
                visited[i + 1] = True
                explored[i + 1] = True
                while len(queue) != 0:
                    top = queue[0]
                    queue = queue[1:]
                    for v in connection[top]:
                        if visited[v] == False:
                            visited[v] = True
                            explored[v] = True
                            queue.append(v)
        return region
