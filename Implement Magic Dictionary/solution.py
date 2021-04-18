class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = defaultdict(lambda:[])

    def buildDict(self, dictionary):
        """
        :type dictionary: List[str]
        :rtype: None
        """
        
        for word in dictionary:
            self.dict[word] = True
            n = len(word)
            for i in range(0,n):
                new_word = word[0:i] + '#' + word[i + 1:] 
                self.dict[new_word].append(word)
                
    def search(self, searchWord):
        """
        :type searchWord: str
        :rtype: bool
        """
        n = len(searchWord) 
        for i in range(0,n):
            search = searchWord[0:i] + '#' + searchWord[i + 1:] 
            for match in self.dict[search]:
                if match != searchWord:
                    return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
