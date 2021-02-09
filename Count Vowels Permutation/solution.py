class Solution(object):
    move = {}
    n = 0
    cnt = 0

    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        pa = 1
        pe = 1
        pi = 1
        po = 1
        pu = 1
        ca = 1
        ce = 1
        ci = 1
        co = 1
        cu = 1
        for i in range(1, n):
            ca = pe + pi + pu
            ce = pa + pi
            ci = pe + po
            co = pi
            cu = pi + po
            pa = ca
            pe = ce
            pi = ci
            po = co
            pu = cu
        return (ca + ce + ci + co + cu) % 1000000007
