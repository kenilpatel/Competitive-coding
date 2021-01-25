class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        ina = -1
        non_a = []
        if len(palindrome) == 1:
            return ""
        for i in range(0, len(palindrome)):
            if palindrome[i] == 'a':
                ina = i
            else:
                non_a.append(i)
        for index in non_a:
            new_str = copy.deepcopy(palindrome)
            new_str = new_str[0:index] + 'a' + new_str[index+1:]
            if new_str != new_str[::-1]:
                return new_str
        new_str = copy.deepcopy(palindrome)
        new_str = new_str[0:ina] + 'b' + new_str[ina+1:]
        return new_str
