import heapq
class Solution(object):
    def maximumScore(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        stones = [a,b,c]
        ans = min(a,b,c)  
        if ans == a:
            new_list = [-b,-c]
        elif ans == b:
            new_list = [-a,-c]
        else:
            new_list = [-a,-b] 
        heapq.heapify(new_list)
        steps = ans
        while steps != 0:
            x = -heapq.heappop(new_list)
            x -= 1
            heapq.heappush(new_list,-x)
            steps -= 1
        # print(new_list)
        return ans - max(new_list)
        
