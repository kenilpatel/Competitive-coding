class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i = 0 
        end = len(strs[0])
        cur = strs[0]
        if len(strs) == 1:
            return cur
            
        for i in range(1,len(strs)):
            end = min(len(strs[i]),end)   
            for j in range(0,end): 
                if strs[i][j] == cur[j]:
                    pass
                else: 
                    end = j
                    break
            if end == 0:
                return ""
            cur = cur[0:end]  
        return cur
        
