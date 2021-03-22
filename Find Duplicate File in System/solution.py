class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        hashmap = defaultdict(lambda:[[],0])
        for entry in paths:
            values = entry.split()
            path = values[0]
            files = values[1:]
            for file_n in files:
                name,content = file_n.split('(')
                content = content.replace(')','')
                hashmap[content][0].append(path + '/' + name)
                hashmap[content][1] += 1
        ans = []
        for li,count in hashmap.values():
            if count > 1:
                ans.append(li)
        return ans
        
