class Solution(object):
    track_dict = {}

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.get_count(s)

    def get_count(self, number):
        if number in self.track_dict.keys():
            return self.track_dict[number]
        if "0" == number[0]:
            return 0
        if len(number) == 1:
            if int(number) >= 1 and int(number) <= 26:
                return 1
            else:
                return 0
        if len(number) == 2:
            count = 0
            if int(number) >= 1 and int(number) <= 26:
                count = count + 1
            if int(number[0]) >= 1 and int(number[0]) <= 26:
                if int(number[1]) >= 1 and int(number[1]) <= 26:
                    count = count + 1
            return count
        n1 = number[0]
        n2 = number[0:2]
        count = 0
        if int(n1) >= 1 and int(n1) <= 26:
            cnt = self.get_count(number[1:])
            if cnt >= 1:
                count = count + cnt
        if int(n2) >= 1 and int(n2) <= 26:
            cnt = self.get_count(number[2:])
            if cnt >= 1:
                count = count + cnt
        self.track_dict[number] = count
        return count
