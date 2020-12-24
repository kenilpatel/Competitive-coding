class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        list_digit = list(str(n))
        index_break = -1
        for i in range(len(list_digit)-1, 0, -1):
            if int(list_digit[i]) > int(list_digit[i-1]):
                index_break = i - 1
                break
        if index_break == -1:
            return -1
        else:
            index_replace = 0
            for i in range(index_break + 1, len(list_digit)):
                if(list_digit[index_break] < list_digit[i]):
                    index_replace = i
            print(index_break, index_replace)
            temp = list_digit[index_break]
            list_digit[index_break] = list_digit[index_replace]
            list_digit[index_replace] = temp
            x = list_digit[0:index_break + 1]
            y = list_digit[index_break + 1:]
            final_digit = x + sorted(y)
            final_digit = int("".join(final_digit))
            return final_digit if final_digit < 2147483647 else -1