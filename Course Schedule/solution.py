class Solution(object):
    def get(self):
        return 0

    def getl(self):
        return []

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        zero_set = []
        pre_req_cnt = defaultdict(self.get)
        link = defaultdict(self.getl)
        for tup in prerequisites:
            link[tup[1]].append(tup[0])
            pre_req_cnt[tup[0]] += 1
        for key in range(0, numCourses):
            if pre_req_cnt[key] == 0:
                zero_set.append(key)
        while numCourses != 0 and zero_set:
            course = zero_set[0]
            zero_set = zero_set[1:]
            for l in link[course]:
                pre_req_cnt[l] -= 1
                if pre_req_cnt[l] == 0:
                    zero_set.append(l)
            numCourses -= 1
        return numCourses == 0
