class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        att = {}
        rem = {}
        x = len(tasks)
        if n == 0:
            return x
        for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            att[i] = 0
            rem[i] = 0
        for i in tasks:
            rem[i] += 1

        at = 1

        while x != 0:
            minatt = float('inf')
            alpha = ""
            flag = 0
            pralpha = ""
            crcnt = 0
            for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                if at >= att[i] and rem[i] > 0:
                    crcnt = max(crcnt, rem[i])
                    if crcnt == rem[i]:
                        pralpha = i
                    flag = 1
                if att[i] != 0 and rem[i] > 0:
                    minatt = min(att[i], minatt)
                    if minatt == att[i]:
                        alpha = i
            x = x - 1
            if flag == 1:
                att[pralpha] = at + n + 1
                rem[pralpha] -= 1
                if x == 0:
                    return at
                at += 1
            else:
                at = minatt
                att[alpha] = at + n + 1
                rem[alpha] -= 1
                if x == 0:
                    return minatt
                at += 1
        return at
