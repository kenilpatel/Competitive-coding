class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        process_graph = defaultdict(lambda: [])
        for i in range(0, len(pid)):
            process_graph[ppid[i]].append(pid[i])
        process_killed = []
        q = [kill]
        while q:
            top = q.pop(0)
            process_killed.append(top)
            for c in process_graph[top]:
                q.append(c)
        return process_killed
