class Solution(object):
    memo = None

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.memo = {}
        x = self.getparts(s)
        return x

    def getparts(self, s):
        if s in self.memo:
            return self.memo[s]
        if len(s) == 1:
            self.memo[s] = [[s]]
            return [[s]]
        else:
            ans_list = []
            for i in range(1, len(s)):
                left = s[0:i]
                right = s[i:]
                local_ans = []
                if left != "" and right != "":
                    if left == left[::-1]:
                        local_ans.append(left)
                        for c in self.getparts(right):
                            ans_list.append(local_ans + c)
            if s == s[::-1]:
                ans_list.append([s])
            self.memo[s] = ans_list
            return ans_list
