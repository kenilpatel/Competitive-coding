class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        q = [0]
        self.n = len(graph) - 1
        self.paths = []
        def dfs(node,path):
            if node == self.n:
                self.paths.append(path)
            else:
                for c in graph[node]:
                    dfs(c,path + [c])
        dfs(0,[0])
        return self.paths
