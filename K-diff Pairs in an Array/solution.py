class Solution(object):
    def get(self):
        return 0
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dd = defaultdict(self.get)
        for i in nums:
            dd[i] += 1
        ans_set = set()
        for i in nums:
            dd[i] -= 1
            x1 = k + i
            x2 = -k + i
            x3 = i - k
            x4 = i + k
            s = (x1,x2,x3,x4)
            for en in s:
                if dd[en] > 0:
                    if i < en:
                        ans_set.add((i,en))
                    else:
                        ans_set.add((en,i))
        return len(ans_set)