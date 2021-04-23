class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        self.child = defaultdict(lambda:[])
        for idx,ele in enumerate(manager):
            self.child[ele].append(idx)
        self.ans = 0 
        def dfs(root,time):
            self.ans = max(self.ans,time)
            for c in self.child[root]:
                dfs(c,time + informTime[root])
        dfs(headID,0)
        return self.ans
