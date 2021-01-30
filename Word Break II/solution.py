class Solution(object):
    wd = None
    memo = None

    def getd(self):
        return -1

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.wd = set(wordDict)
        self.memo = defaultdict(self.getd)
        return self.get(s)

    def get(self, x):
        if self.memo[x] != -1:
            return self.memo[x]
        if x in self.wd:
            self.memo[x] = [x]
            ans = set()
            ans.add(x)
            for i in range(0, len(x)):
                left = x[0:i]
                right = x[i:]
                if right != "" and left != "" and left in self.wd:
                    if self.memo[left] == -1:
                        list1 = self.get(left)
                    else:
                        list1 = self.memo[left]
                    if self.memo[right] == -1:
                        list2 = self.get(right)
                    else:
                        list2 = self.memo[right]
                    if len(list1) >= 1 and len(list2) >= 1:
                        for on in list1:
                            for tw in list2:
                                ans.add(on + " " + tw)
            self.memo[x] = ans
            return ans
        else:
            ans = set()
            for i in range(0, len(x)):
                left = x[0:i]
                right = x[i:]
                if right != "" and left != "" and left in self.wd:
                    if self.memo[left] == -1:
                        list1 = self.get(left)
                    else:
                        list1 = self.memo[left]
                    if self.memo[right] == -1:
                        list2 = self.get(right)
                    else:
                        list2 = self.memo[right]
                    if len(list1) >= 1 and len(list2) >= 1:
                        for on in list1:
                            for tw in list2:
                                ans.add(on + " " + tw)
            self.memo[x] = ans
            return ans
