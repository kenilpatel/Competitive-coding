class Solution(object):
    def get(self):
        return None

    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        set_word = set(words)
        len_dict = defaultdict(self.get)
        q = []
        for entry in words:
            q.append((entry, 1))
        ans = 1
        while q:
            top, length = q.pop(0)
            if ans < length:
                ans = length
            for pos in "abcdefghijklmnopqrstuvwxyz":
                for i in range(0, len(top) + 1):
                    new_word = top[0:i] + pos + top[i:]
                    if new_word in set_word:
                        q.append((new_word, length + 1))
        return ans
