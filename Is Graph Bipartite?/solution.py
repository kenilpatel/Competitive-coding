class Solution(object):
    label = None
    graph = None
    ans = True

    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        self.label = defaultdict(lambda: "-")
        self.graph = graph
        self.ans = True
        for i in range(0, len(graph)):
            if self.label[i] == "-":
                self.dfs(i, "e")
        return self.ans

    def dfs(self, source, pre_label):
        if self.label[source] == pre_label:
            self.ans = False
        else:
            if self.label[source] == "-":
                if pre_label == "o":
                    self.label[source] = "e"
                else:
                    self.label[source] = "o"
                for c in self.graph[source]:
                    self.dfs(c, self.label[source])
