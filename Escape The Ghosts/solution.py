class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        start = [0, 0]
        min_step_p = abs(target[0] - start[0]) + abs(target[1] - start[1])
        for g in ghosts:
            min_g = abs(target[0] - g[0]) + abs(target[1] - g[1])
            if min_step_p >= min_g:
                return False
        return True
