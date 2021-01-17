class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        neg = 0
        if len(s) == 0:
            return 0
        else:
            if s[0] == "-":
                neg = 1
                s = s[1:]
            elif s[0] == "+":
                neg = 0
                s = s[1:]
        digit = ""
        for i in range(0, len(s)):
            char = s[i]
            if char == "0" or char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9":
                digit += char
            else:
                break

        if digit == "":
            return 0
        else:
            digit = int(digit)
            if neg == 1:
                digit = -digit
                return -2**31 if digit < -2**31 else digit
            else:
                return 2**31 - 1 if digit > 2**31 - 1 else digit
