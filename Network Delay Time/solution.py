import heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph = defaultdict(lambda:[])
        time = {}
        for u in range(1,n + 1):
            time[u] = float('inf') 
        for u,v,t1 in times:
            graph[u].append((v,t1))
            
        q = [(0,k)]
        heapq.heapify(q)
        visited = set() 
        while q:
            t,top = heapq.heappop(q)  
            visited.add(top)
            time[top] = min(t,time[top])
            for c,tc in graph[top]:
                if c not in visited: 
                    heapq.heappush(q,(t + tc,c))
        ans = max(time.values())
        if ans == float('inf'):
            return -1
        else:
            return ans
            
        
