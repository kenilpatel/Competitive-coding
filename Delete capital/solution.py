class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        ans = True
        first = True
        second = True
        all_c = False
        x = 0
        for char in word:
            asc = ord(char)
            if x == 0:
                if(asc >= 97 and asc <= 122):
                    first = False
            elif x == 1:
                if(asc >= 97 and asc <= 122):
                    second = False
            else:
                if second == False:
                    if asc >= 65 and asc <= 90:
                        all_c = True
                        break
                    else:
                        all_c = False
                else:
                    if asc >= 97 and asc <= 122:
                        all_c = False
                        break
                    else:
                        all_c = True
            x = x + 1
        if len(word) > 2:
            if first == second and second == all_c:
                return True
            else:
                if first == True and second == False and all_c == False:
                    return True
                else:
                    return False
        else:
            if(x == 1):
                return True
            else:
                return True if first == second or first == True and second == False else False
