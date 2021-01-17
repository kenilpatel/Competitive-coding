class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        dict_no = {("a", 1): 1, ("e", 1): 1, ("i", 1): 1, ("o", 1): 1, ("u", 1): 1}
        ans = 5
        for i in range(2, n + 1):
            dict_no[("a", i)] = dict_no[("a", i - 1)] + dict_no[("e", i - 1)] + \
                dict_no[("i", i - 1)] + dict_no[("o", i - 1)] + \
                dict_no[("u", i - 1)]
            dict_no[("e", i)] = dict_no[("e", i - 1)] + dict_no[("i",
                                                                 i - 1)] + dict_no[("o", i - 1)] + dict_no[("u", i - 1)]
            dict_no[("i", i)] = dict_no[("i", i - 1)] + \
                dict_no[("o", i - 1)] + dict_no[("u", i - 1)]
            dict_no[("o", i)] = dict_no[("o", i - 1)] + dict_no[("u", i - 1)]
            dict_no[("u", i)] = dict_no[("u", i - 1)]
            ans = dict_no[("a", i)] + dict_no[("e", i)] + \
                dict_no[("i", i)] + dict_no[("o", i)] + dict_no[("u", i)]
        return ans
