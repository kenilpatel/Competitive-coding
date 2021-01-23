import re


class Solution(object):
    def get(self):
        return 0

    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        count_dict = defaultdict(self.get)
        paragraph = paragraph.lower()
        paragraph = re.sub(r"[!?',;.]", " ", paragraph)
        for w in banned:
            paragraph = re.sub(w, "", paragraph)
        paragraph = paragraph.split()
        for w in paragraph:
            count_dict[w] += 1
        ans = ""
        count = 0
        for key in count_dict.keys():
            if count_dict[key] > count:
                count = count_dict[key]
                ans = key
        return ans
