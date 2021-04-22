import heapq
class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        half = n / 2
        cur_s = n 
        count = defaultdict(lambda:0)
        for i in arr:
            count[i] += 1
        arr = []
        heapq.heapify(arr)
        for key,val in count.items(): 
            heapq.heappush(arr,(-val,key))
        ans = 0 
        while cur_s > half: 
            count,val = heapq.heappop(arr)
            cur_s += count
            ans += 1
        return ans
