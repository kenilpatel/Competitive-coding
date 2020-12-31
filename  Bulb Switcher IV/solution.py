class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        compare = "0"
        flip = 0
        for i in target:
            if i != compare:
                flip = flip + 1
                if compare == "0":
                    compare = "1"
                else:
                    compare = "0"
        return flip
