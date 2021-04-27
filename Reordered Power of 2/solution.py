class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        power = 0 
        res = 0
        powmap = defaultdict(lambda:[])
        while res <= 10 ** 9:
            res = 2 ** power
            powmap[len(str(res))].append(str(res))
            power += 1 
        n = str(n)
        n = sorted(n,reverse = True)
        for comb in powmap[len(n)]:
            if sorted(comb,reverse = True) == n:
                return True
        return False
