class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        score = []
        last = 0
        for i in range(0, len(ops)):
            if ops[i] == "+":
                score.append(score[last - 1] + score[last - 2])
                last += 1
            elif ops[i] == "D":
                score.append(score[last - 1]*2)
                last += 1
            elif ops[i] == "C":
                score = score[0:last - 1]
                last -= 1
            else:
                score.append(int(ops[i]))
                last += 1
        return sum(score)
