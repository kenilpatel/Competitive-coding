class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        nd1 = 0
        n = len(num1) - 1
        for i in range(0, n + 1):
            if num1[i] == '9':
                nd1 = nd1 + 9 * (10 ** (n - i))
            elif num1[i] == '8':
                nd1 = nd1 + 8 * (10 ** (n - i))
            elif num1[i] == '7':
                nd1 = nd1 + 7 * (10 ** (n - i))
            elif num1[i] == '6':
                nd1 = nd1 + 6 * (10 ** (n - i))
            elif num1[i] == '5':
                nd1 = nd1 + 5 * (10 ** (n - i))
            elif num1[i] == '4':
                nd1 = nd1 + 4 * (10 ** (n - i))
            elif num1[i] == '3':
                nd1 = nd1 + 3 * (10 ** (n - i))
            elif num1[i] == '2':
                nd1 = nd1 + 2 * (10 ** (n - i))
            elif num1[i] == '1':
                nd1 = nd1 + 1 * (10 ** (n - i))
            elif num1[i] == '0':
                nd1 = nd1 + 0 * (10 ** (n - i))
        nd2 = 0
        m = len(num2) - 1
        for i in range(0, m + 1):
            if num2[i] == '9':
                nd2 = nd2 + 9 * (10 ** (m - i))
            elif num2[i] == '8':
                nd2 = nd2 + 8 * (10 ** (m - i))
            elif num2[i] == '7':
                nd2 = nd2 + 7 * (10 ** (m - i))
            elif num2[i] == '6':
                nd2 = nd2 + 6 * (10 ** (m - i))
            elif num2[i] == '5':
                nd2 = nd2 + 5 * (10 ** (m - i))
            elif num2[i] == '4':
                nd2 = nd2 + 4 * (10 ** (m - i))
            elif num2[i] == '3':
                nd2 = nd2 + 3 * (10 ** (m - i))
            elif num2[i] == '2':
                nd2 = nd2 + 2 * (10 ** (m - i))
            elif num2[i] == '1':
                nd2 = nd2 + 1 * (10 ** (m - i))
            elif num2[i] == '0':
                nd2 = nd2 + 0 * (10 ** (m - i))
        return str(nd1 + nd2)
