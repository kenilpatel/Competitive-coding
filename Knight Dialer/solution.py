class Solution(object):
    def get(self):
        return 0

    def knightDialer(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            5: []
        }
        count_dict = defaultdict(self.get)
        for i in range(0, 10):
            count_dict[i] += 1
        n = n - 1
        while n != 0:
            temp_dict = defaultdict(self.get)
            for key in count_dict.keys():
                for c in start[key]:
                    temp_dict[c] += count_dict[key]
            count_dict = temp_dict
            n = n - 1
        return sum(count_dict.values()) % 1000000007
