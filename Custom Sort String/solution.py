import collections


class Solution(object):
    def getorder(self):
        return 0

    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        order = defaultdict(self.getorder)
        for i in range(0, len(S)):
            order[S[i]] = i
        custom_list = []
        for i in T:
            custom_list.append((i, order[i]))
        return "".join(map(lambda x: x[0], sorted(custom_list, key=lambda x: x[1])))
