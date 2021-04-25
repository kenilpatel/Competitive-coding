class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        bank = set(bank)
        q = [(start,0)]
        visited = set()
        visited.add(q[0][0])
        while q:
            top,step = q.pop(0)
            if top == end:
                return step
            for i in range(0,len(top)):
                new1 = top[0:i] + 'T' +top[i + 1:]
                new2 = top[0:i] + 'A' +top[i + 1:]
                new3 = top[0:i] + 'C' +top[i + 1:]
                new4 = top[0:i] + 'G' +top[i + 1:]
                if new1 not in visited and new1 in bank:
                    visited.add(new1)
                    q.append((new1,step + 1))
                if new2 not in visited and new2 in bank:
                    visited.add(new2)
                    q.append((new2,step + 1))
                if new3 not in visited and new3 in bank:
                    visited.add(new3)
                    q.append((new3,step + 1))
                if new4 not in visited and new4 in bank:
                    visited.add(new4)
                    q.append((new4,step + 1))
        return -1
            
                
                
