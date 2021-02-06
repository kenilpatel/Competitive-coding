class Solution(object):
    posset = None
    ans = 0

    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        self.posset = []
        self.dfs("", arr)
        # print(self.posset)
        return self.ans

    def dfs(self, string, arr):
        if self.ans < len(string):
            self.ans = len(string)
        self.posset.append(string)
        for i in range(0, len(arr)):
            new_c = set(string + arr[i])
            if len(new_c) == len(string + arr[i]):
                self.dfs(string + arr[i], arr[i + 1:])
