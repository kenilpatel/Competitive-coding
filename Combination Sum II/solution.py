class Solution(object):
    tlist = None
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.tlist = []
        candidates.sort()
        if sum(candidates) == target:
            return [candidates]
        elif sum(candidates) > target:
            self.generate(candidates,target,[],0)
            dict = {}
            for i in self.tlist:
                dict[str(i)] = i
            return  dict.values()
        else:
            return []
    def generate(self,candidate,target,tlist_l,tlistsum_l):
        if target == tlistsum_l:
            self.tlist.append(tlist_l)
        elif tlistsum_l < target:
            for i in range(0,len(candidate)):
                self.generate(candidate[i+1:],target,tlist_l + [candidate[i]],tlistsum_l + candidate[i])