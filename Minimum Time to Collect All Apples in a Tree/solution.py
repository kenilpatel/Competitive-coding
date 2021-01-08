import collections


class Solution(object):
    edge_dict = None
    graph = None
    apple = None
    visited = None

    def getval(self):
        return 0

    def getlist(self):
        return []

    def getbool(self):
        return False

    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        self.edge_dict = defaultdict(self.getval)
        self.visited = defaultdict(self.getbool)
        self.graph = defaultdict(self.getlist)
        self.apple = hasApple
        for e in edges:
            self.graph[e[0]].append(e[1])
            self.graph[e[1]].append(e[0])
        self.visited[0] = True
        self.dfs(0, [])
        return len(self.edge_dict) * 2

    def dfs(self, node, edge_point):
        if self.apple[node] == True:
            for e in edge_point:
                self.edge_dict[str(e)] = True
        for child in self.graph[node]:
            if self.visited[child] == False:
                edge = [node, child]
                self.visited[child] = True
                self.dfs(child, edge_point + [edge])
