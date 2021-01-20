class Solution(object):
    def getlist(self):
        return []

    def getcount(self):
        return 0

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        taken = 0
        edges = defaultdict(self.getlist)
        zero = []
        count = defaultdict(self.getcount)
        for e in prerequisites:
            edges[e[1]].append(e[0])
            count[e[0]] += 1
        for i in range(0, numCourses):
            if count[i] == 0:
                zero.append(i)
        order = []
        while len(zero) != 0:
            course = zero[0]
            zero = zero[1:]
            taken += 1
            order.append(course)
            for v in edges[course]:
                count[v] -= 1
                if count[v] == 0:
                    zero.append(v)
        if taken == numCourses:
            return order
        else:
            return []
