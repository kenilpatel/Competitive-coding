class Solution(object):
    def get(self):
        return 0

    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        cnt = defaultdict(self.get)
        for i in range(0, len(time)):
            time[i] = time[i] % 60
        for i in time:
            cnt[i] += 1
        tot_pair = 0
        for i in time:
            cnt[i] -= 1
            if i == 0:
                tot_pair += cnt[0]
            else:
                target = 60 - i
                tot_pair += cnt[target]
        return tot_pair
