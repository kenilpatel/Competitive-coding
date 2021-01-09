import collections


class Solution(object):
    def getval(self):
        return False

    def getlist(self):
        return []

    def getset(self):
        return set()

    def int(self):
        return 0

    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        original = defaultdict(self.getval)
        secondary = defaultdict(self.getlist)
        vowel = ['a', 'e', 'i', 'o', 'u']
        vowel_dict = defaultdict(self.int)
        subs = defaultdict(self.getlist)
        for v in vowel:
            vowel_dict[v] = 1
        for word in wordlist:
            original[word] = True
            secondary[word.lower()].append(word)
            subs[re.sub('[aeiou]', 'a', word.lower())].append(word)
        op = []
        for query in queries:
            if original[query] == True:
                op.append(query)
                continue
            seco_list = secondary[query.lower()]
            if len(seco_list) != 0:
                op.append(seco_list[0])
                continue
            else:
                query = query.lower()
                query = re.sub('[aeiou]', 'a', query)
                seco_list = subs[query]
                if len(seco_list) != 0:
                    op.append(seco_list[0])
                    continue
                else:
                    op.append("")
        return op
