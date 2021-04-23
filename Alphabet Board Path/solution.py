class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        x = [(-5,"U"),(-1,"L"),(5,"D"),(1,"R")]
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        
        path = ""
        self.alpha_set = set("absdefghijklmnopqrstuvwxyz") 
        pos = 'a'
        def bfs(find,start):
            q = [(start,"")]
            visited = set()
            visited.add(start)
            s1 = set('afkpuz')
            s2 = set('ejoty')
            s3 = set('zvwxy')
            s4 = set('abcde')
            while q:
                top,path = q.pop(0) 
                if top == find: 
                    return path + "!",
                for i,d in x:
                    if top not in s1 and i == -1:
                        child = chr(ord(top) + i) 
                        q.append((child,path + d)) 
                    if top not in s2 and i == 1:
                        child = chr(ord(top) + i) 
                        q.append((child,path + d)) 
                    if top not in s3 and i == 5:
                        child = chr(ord(top) + i)
                        q.append((child,path + d)) 
                    if top not in s4 and i == -5:
                        child = chr(ord(top) + i)
                        q.append((child,path + d)) 
        n = len(target)
        path = bfs(target[0],"a")
        for i in range(1,n):
            path += bfs(target[i],target[i - 1])
        return "".join(path)
            
