class Solution(object):
    def get(self):
        return []

    def geti(self):
        return -1

    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(self.get)
        final_visited = set([0])
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        visited_by = defaultdict(self.geti)
        visited_by[0] = 99
        q = [0]
        while q:
            top = q.pop(0)
            final_visited.add(top)
            for c in graph[top]:
                if c != 0:
                    if visited_by[c] == -1:
                        q.append(c)
                        visited_by[c] = top
                    else:
                        if visited_by[c] != top and visited_by[top] != c:
                            return False
        if len(final_visited) == n:
            return True
        else:
            return False
