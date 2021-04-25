class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """   
        dis_set = {}
        for u,v in edges: 
            dis_set[u] = u
            dis_set[v] = v
        
        def findparent(node):
            while dis_set[node] != node:
                node = dis_set[node] 
            return node 
            
        
        for u,v in edges:
            us = findparent(u)  
            vs = findparent(v) 
            if us == vs:
                return [u,v]
            dis_set[us] = vs 
            
        
            
