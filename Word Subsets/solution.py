class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        set_b = set("".join(B)) 
        globald = defaultdict(lambda:0)
        for word in B:
            d = defaultdict(lambda:0)
            for char in word:
                d[char] += 1
            for char in word:
                globald[char] = max(globald[char],d[char])
        dict_a = []
        for word in A:
            d = defaultdict(lambda:0)
            for char in word:
                d[char] += 1
            dict_a.append(d)
        ans = []
        for i in range(0,len(A)):
            word = A[i]
            for word in word:
                d = defaultdict(lambda:0)
                for char in word:
                    d[char] += 1
                dict_a.append(d)
            found = True
            for key in globald.keys():
                if globald[key] > dict_a[key]:
                    found = False
                    break
            if found:
                ans.append(word)
        return ans
