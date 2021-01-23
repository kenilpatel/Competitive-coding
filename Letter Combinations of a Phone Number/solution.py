class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans = []
        digit = {}
        digit["2"] = ["a", "b", "c"]
        digit["3"] = ["d", "e", "f"]
        digit["4"] = ["g", "h", "i"]
        digit["5"] = ["j", "k", "l"]
        digit["6"] = ["m", "n", "o"]
        digit["7"] = ["p", "q", "r", "s"]
        digit["8"] = ["t", "u", "v"]
        digit["9"] = ["w", "x", "y", "z"]
        ans = []
        for i in digits:
            if len(ans) == 0:
                ans = digit[i]
            else:
                new_ans = []
                for a in ans:
                    for c in digit[i]:
                        new_ans.append(a+c)
                ans = new_ans
        return ans
