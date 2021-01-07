class Solution(object):
    def getval(self):
        return False

    def getval1(self):
        return -1

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        track_dict = defaultdict(self.getval)
        last_index = defaultdict(self.getval1)
        i = 0
        while i != len(s):
            char = s[i]
            if track_dict[char] == True:
                i = last_index[char]
                if max_len < len(track_dict.keys()):
                    max_len = len(track_dict.keys())
                track_dict = defaultdict(self.getval)
            else:
                track_dict[char] = True
                last_index[char] = i
            i = i + 1
        if max_len < len(track_dict.keys()):
            max_len = len(track_dict.keys())
        return max_len
