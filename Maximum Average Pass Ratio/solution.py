import heapq
class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        probab = []
        for i,x in enumerate(classes): 
            cur = float(x[0]) / float(x[1])
            new = float(x[0] + 1) / float(x[1] + 1)
            probab.append((cur - new,i))
        heapq.heapify(probab)
        while extraStudents != 0:
            idx = heapq.heappop(probab)[1]
            classes[idx][0] += 1
            classes[idx][1] += 1
            x = classes[idx]
            cur = float(x[0]) / float(x[1])
            new = float(x[0] + 1) / float(x[1] + 1)
            heapq.heappush(probab,(cur - new,idx))
            extraStudents -= 1
        ans = 0 
        for i,j in classes:
            ans += float(i) / float(j)
        return ans / len(classes)
