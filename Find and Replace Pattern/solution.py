class Solution(object):
    def getd(self):
        return ""
    def getb(self):
        return False
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        ans = []
        for w in words:
            if len(w) == len(pattern):
                word_dict = defaultdict(self.getd)
                match_check = defaultdict(self.getb)
                gotit = True
                for i in range(0,len(w)):
                    cur_point = word_dict[w[i]]
                    if cur_point == "":
                        if match_check[pattern[i]] == False:
                            word_dict[w[i]] = pattern[i]
                            match_check[pattern[i]] = True
                        else:
                            gotit = False
                            break
                    else:
                        if cur_point != pattern[i]:
                            gotit = False
                            break
                if gotit == True:
                    ans.append(w)
        return ans
