class Solution(object):
    def queryString(self, S, N):
        for n in xrange(1, N+1):
            if self.toBinary(n) in S:
                continue
            else:
                return False

        return True

    def toBinary(self, n):
        digits = []
        while n:
            digits.append(str(n % 2))
            n //= 2
        return ''.join(digits[::-1])
