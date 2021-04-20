import heapq
class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = []
        heapq.heapify(a)
        s = set(s)
        for i in s:
            if i not in "abcdefghijklmnopqrstuvwxyz":
                heapq.heappush(a,-int(i)) 
        try:
            heapq.heappop(a)
            return -heapq.heappop(a)
        except:
            return -1
        
            
