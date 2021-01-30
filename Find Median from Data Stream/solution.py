from collections import OrderedDict
import heapq
class MedianFinder(object):
    size = 0
    lowerhalf = []
    upperhalf = []
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.size = 0
        self.num_list = []
        self.lowerhalf = []
        self.upperhalf = []
        heapq.heapify(self.lowerhalf)
        heapq.heapify(self.upperhalf)
    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """

        if len(self.lowerhalf) == 0:
            heapq.heappush(self.lowerhalf, -num)
            return
        if num <= -self.lowerhalf[0]:
            heapq.heappush(self.lowerhalf, -num)
        else:
            heapq.heappush(self.upperhalf, num)
        if len(self.lowerhalf) - len(self.upperhalf) == 2:
            heapq.heappush(self.upperhalf, - heapq.heappop(self.lowerhalf))
        elif len(self.upperhalf) - len(self.lowerhalf) == 2:
            heapq.heappush(self.lowerhalf, - heapq.heappop(self.upperhalf))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.lowerhalf) == len(self.upperhalf):
            return (- self.lowerhalf[0] + self.upperhalf[0] )/2.0
        elif len(self.lowerhalf) > len(self.upperhalf):
            return -float(self.lowerhalf[0])
        else:
            return float(self.upperhalf[0])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()