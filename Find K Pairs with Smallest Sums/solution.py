import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        i = 0 
        j = 0 
        n = len(nums1)
        m = len(nums2)
        pairs = []
        heapq.heapify(pairs)
        for i in range(n):
            for j in range(m):
                heapq.heappush(pairs,(nums1[i] + nums2[j],[nums1[i],nums2[j]]))
        ans = [] 
        while k != 0 and pairs:
            s,p = heapq.heappop(pairs)
            ans.append(p)
            k -= 1
        return ans
                            
