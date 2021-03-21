import math
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = ''.join(s.split())
        n = len(s)
        i = 0
        neg = 0
        stack = []
        while i < n:    
            if s[i] == '+':
                pass
            elif s[i] == "-":
                neg = 1
            elif s[i] == '*':
                pop_num = stack.pop()

                i = i + 1
                num = s[i]
                while i + 1 < n and s[i + 1].isdigit():
                    num += s[i + 1]
                    i += 1
                num = int(num)
                stack.append(num * pop_num)
            elif s[i] == '/': 
                pop_num = stack.pop()  
                i = i + 1
                num = s[i]
                while i + 1 < n and s[i + 1].isdigit():
                    num += s[i + 1]
                    i += 1
                num = int(num) 
                res = float(float(pop_num) / float(num)) 
                if res > 0:
                    stack.append(math.floor(res))
                else:
                    stack.append(math.ceil(res))
            else:
                num = s[i]
                while i + 1 < n and s[i + 1].isdigit():
                    num += s[i + 1]
                    i += 1  
                if neg == 1:
                    stack.append(int(num) * -1)
                    neg = 0
                else:
                    stack.append(int(num))
            i += 1
        return int(sum(stack))
