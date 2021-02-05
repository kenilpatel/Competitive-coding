class Solution(object):
    roti = None

    def __init__(self):
        self.roti = {}
        self.roti[0] = ""
        self.roti[1] = 'I'
        self.roti[2] = 'II'
        self.roti[3] = "III"
        self.roti[4] = 'IV'
        self.roti[5] = 'V'
        self.roti[6] = 'VI'
        self.roti[7] = 'VII'
        self.roti[8] = 'VIII'
        self.roti[9] = 'IX'
        self.roti[10] = 'X'
        self.roti[20] = 'XX'
        self.roti[30] = 'XXX'
        self.roti[40] = 'XL'
        self.roti[50] = 'L'
        self.roti[60] = 'LX'
        self.roti[70] = 'LXX'
        self.roti[80] = 'LXXX'
        self.roti[90] = 'XC'
        self.roti[100] = 'C'
        self.roti[200] = 'CC'
        self.roti[300] = 'CCC'
        self.roti[400] = 'CD'
        self.roti[500] = 'D'
        self.roti[600] = 'DC'
        self.roti[700] = 'DCC'
        self.roti[800] = 'DCCC'
        self.roti[900] = 'CM'
        self.roti[1000] = 'M'
        self.roti[2000] = 'MM'
        self.roti[3000] = 'MMM'

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        nums = str(num)
        ln = len(nums)
        ans = ""
        for i in range(0, ln):
            ans += self.roti[int(nums[i]) * 10 ** (ln - i - 1)]
        return ans
