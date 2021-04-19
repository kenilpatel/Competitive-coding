class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = set()
        n = len(nums)
        ans = 0
        for i in range(n):
            if i not in visited:
                q = [i]
                l = 0
                visited.add(i)
                while q:
                    top = q.pop(0)
                    l += 1
                    if nums[top] not in visited:
                        q.append(nums[top])
                        visited.add(nums[top])
                ans = max(ans,l)
        return ans
                        
