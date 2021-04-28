class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """ 
        while n != 0:
            x = str(n % 3)
            if x == "2":
                return False
            n = int(n / 3) 
        return True
                
                
