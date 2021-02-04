class Solution(object):
    ans = None
    candidates = None

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.candidates = candidates
        self.ans = set()
        self.dfs(0, target, [])
        return self.ans

    def dfs(self, sumt, target, comblist):
        if sumt > target:
            return
        if sumt == target:
            self.ans.add(tuple(comblist))
            return
        for i in range(0, len(self.candidates)):
            idx = bisect.bisect_right(comblist, self.candidates[i])
            temp_comb = comblist[0:idx] + [self.candidates[i]] + comblist[idx:]
            temp_sum = sumt + self.candidates[i]
            if temp_sum < target:
                self.dfs(temp_sum, target, temp_comb)
            if temp_sum == target:
                self.ans.add(tuple(temp_comb))
