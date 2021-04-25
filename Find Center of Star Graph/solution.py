class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """ 
        count = defaultdict(lambda:0)
        for i,j in edges:
            if count[i] == 1:
                return i
            if count[j] == 1:
                return j
            count[i] += 1
            count[j] += 1 
        
        
