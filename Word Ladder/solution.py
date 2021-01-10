import collections


class Solution(object):
    def getlist(self):
        return set()

    def getbool(self):
        return False

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        masked_dict = defaultdict(self.getlist)
        for word in wordList:
            for i in range(0, len(word)):
                masked = word[0:i] + "#" + word[i+1:]
                masked_dict[masked].add(word)
        queue = [(beginWord, 0)]
        visited = defaultdict(self.getbool)
        visited[beginWord] = True
        lowest_step = 0
        while len(queue) != 0:
            word, depth = queue[0]
            queue = queue[1:]
            if word == endWord:
                return depth + 1
            for i in range(0, len(word)):
                masked = word[0:i] + "#" + word[i+1:]
                if len(masked_dict[masked]) != 0:
                    for w in masked_dict[masked]:
                        if visited[w] == False:
                            visited[w] = True
                            queue.append((w, depth + 1))
        return 0
