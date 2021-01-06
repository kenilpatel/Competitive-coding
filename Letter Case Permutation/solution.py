import collections
import copy
class Solution(object):
    def getval(self):
        return 0
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        S = S.lower()
        queue = [S]
        explored = defaultdict(self.getval)
        explored[S]
        while len(queue) != 0:
            top = queue[0]
            queue = queue[1:]
            for i in range(0,len(top)):
                new_str = copy.deepcopy(top)
                if new_str[i].islower():
                    new_str = new_str[0:i] + new_str[i].upper() + new_str[i+1:]
                    if explored[new_str] == 0:
                        explored[new_str] = 1
                        queue = queue + [new_str]
        return explored.keys()