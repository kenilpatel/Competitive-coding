class Solution(object):
    word_dict = None
    memo = None

    def getbool(self):
        return False

    def get(self):
        return 0

    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        self.memo = defaultdict(self.get)
        for w in words:
            self.memo[w] = 1
        ans = []
        for w in words:
            if self.check(w) == True:
                ans.append(w)
        return ans

    def check(self, word):
        for i in range(0, len(word) - 1):
            left = word[0:i + 1]
            right = word[i + 1:]
            right_bool = False
            if right != "":
                if self.memo[left] == 1:
                    if self.memo[right] == 0:
                        right_bool = self.check(right)
                        self.memo[right] = 1 if right_bool == True else -1
                    else:
                        if self.memo[right] == -1:
                            right_bool = False
                        else:
                            right_bool = True
                    if self.memo[left] == 1 and right_bool == True:
                        return True
        return False
