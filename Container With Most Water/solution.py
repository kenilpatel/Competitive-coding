class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0 
        r = len(height) - 1
        maxans = float('-inf')
        while l < r:
            area = (r -l) * min(height[l],height[r]) 
            maxans = max(area,maxans)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxans
            
