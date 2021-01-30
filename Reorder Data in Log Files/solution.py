class Solution(object):

    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        dig = []
        let = []
        for l in logs:
            l1 = l.split()
            idd, x = l1[0], "".join(l1[1:])
            if x.isnumeric():
                dig.append(l)
            else:
                let.append((" ".join(l1[1:]), idd))
        let = sorted(let)
        let = [i[1] + " " + i[0] for i in let]
        return let + dig
