class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        q = []
        available = [i for i in range(1, n+1)]
        for i in range(1, n + 1):
            q.append(([i], k - 1, i))
        # print(q)
        ans = []
        while len(q) != 0:
            top_list, need, si = q[0]
            q = q[1:]
            if need == 0:
                ans.append(top_list)
            for i in range(si, len(available)):
                if need - 1 <= len(available[i + 1:]) and need > 0:
                    q.append((top_list + [available[i]], need - 1, i + 1))
        return ans
