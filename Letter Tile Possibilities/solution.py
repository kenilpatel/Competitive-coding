class Solution(object):
    ans = None
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """ 
        ls = len(tiles)
        ignore_i = set()
        self.ans = set()
        def dfs(string,ignore_i):
            self.ans.add(string) 
            for i in range(0,ls):
                if i not in ignore_i:
                    x = copy.deepcopy(ignore_i)
                    x.add(i)
                    dfs(string + tiles[i],x)
        dfs("",ignore_i)
        return len(self.ans) - 1
