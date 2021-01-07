import collections
import math


class Solution(object):
    def getval(self):
        return [0, 0, 0]

    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        bound_dict = defaultdict(self.getval)
        num_dict = {}
        atoz = "abcdefghijklmnopqrstuvwxyz"
        for i in range(0, len(atoz)):
            bound_dict[atoz[i]] = [i + 1, i + 1 +
                                   (n - 1) * 1, i + 1 + (n - 1) * 26]
            num_dict[i + 1] = atoz[i]
        if n == 1:
            return num_dict[k]
        for char in atoz:
            if k >= bound_dict[char][1] and k <= bound_dict[char][2]:
                string = ""
                string = string + num_dict[bound_dict[char][0]]
                x = float(float(k - bound_dict[char][0] - (n - 1)) / 25.0)
                # print(x, k - bound_dict[char][0] - (n - 1))
                no_of_a = int(n - 1 - math.ceil(x))
                # print(no_of_a)
                string = string + "a" * no_of_a
                if math.floor(x) == math.ceil(x):
                    string = string + "z" * int(x)
                else:
                    diff = k - bound_dict[char][0] - \
                        no_of_a - 26 * math.floor(x)
                    string = string + num_dict[diff] + "z" * int(math.floor(x))
                return string
