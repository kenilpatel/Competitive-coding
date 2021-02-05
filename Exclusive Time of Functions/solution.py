class Solution(object):
    def get(self):
        return 0

    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        ndict = defaultdict(self.get)
        stack = []
        for x in logs:
            l = x.split(":")
            l[0] = int(l[0])
            l[2] = int(l[2])
            if l[1] == "end":
                x = stack.pop()
                if stack:
                    y = stack.pop()
                    ndict[x[0]] += l[2] + 1 - x[2]
                    y[2] = l[2] + 1
                    stack.append(y)
                else:
                    ndict[x[0]] += l[2] + 1 - x[2]
            if l[1] == "start":
                if stack:
                    x = stack.pop()
                    ndict[x[0]] += l[2] - x[2]
                    stack.append(x)
                stack.append(l)
        ans = [0] * n
        for key in ndict.keys():
            ans[key] = ndict[key]
        return ans
