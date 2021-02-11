class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        q = []
        limit = len(str(N))
        visited = set()
        for i in range(len(choices) - 1, -1, -1):
            q.append((choices[i], choices[i:]))
            visited.add(int(choices[i]))
        pos = []
        max_l = 0
        while q:
            top, choices = q.pop(0)
            topi = int(top)
            if topi <= N:
                if len(top) == limit:
                    return topi
                else:
                    if max_l <= topi:
                        max_l = topi
            for i in range(len(choices) - 1, -1, -1):
                new = top + choices[i]
                new_i = int(new)
                if new_i <= N and new_i not in visited:
                    visited.add(new_i)
                    q.append((new, choices[i:]))
        return max_l
