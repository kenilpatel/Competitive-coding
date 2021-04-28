class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        def check(s,n):
            n = n - 1
            if s[n] == '1':
                for i in range(n):
                    if s[i] == '1':
                        return True
                return False
            else:
                return True
        def odd(s,n):
            n = n - 1
            if s[n] == '1':
                return True
            else:
                return False
        
        def by_two(s):
            s = list(s)
            s.pop()
            return "".join(s)
        
        def plus(s,n):
            vadi = 0
            ans = []
            add = 1
            for i in range(n - 1,-1,-1):
                local = vadi + add + int(s[i]) 
                if local == 2:
                    vadi = 1
                    add = 0 
                else:
                    vadi = 0
                    add = 0 
                ans.append(local % 2)
            if vadi == 1:
                ans.append(1)
            ans = [str(i) for i in ans]
            return "".join(ans[::-1]) 
        step = 0 
        while(check(s,len(s))):
            n = len(s)
            if odd(s,n):
                s = plus(s,n)
            else:
                s = by_two(s)
                
            step += 1
        return step
