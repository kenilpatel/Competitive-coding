class Solution(object):
    route = None
    ans = None

    def get(self):
        return []

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        used_itenary = set()
        route = defaultdict(self.get)
        for i in range(0, len(tickets)):
            route[tickets[i][0]].append((tickets[i][1], i))
        for key in route.keys():
            route[key] = sorted(route[key])
        self.route = route
        self.dfs("JFK", used_itenary, len(tickets), ["JFK"])
        return self.ans

    def dfs(self, from_port, used_itenary, it_left, seq):
        route = self.route
        if it_left == 0:
            self.ans = seq
        else:
            for c in route[from_port]:
                if c[1] not in used_itenary and self.ans == None:
                    ui = copy.deepcopy(used_itenary)
                    ui.add(c[1])
                    self.dfs(c[0], ui, it_left - 1, seq + [c[0]])
