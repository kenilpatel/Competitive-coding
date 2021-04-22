class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums) 
        dp = defaultdict(lambda:-1)
        def dfs(sumt,i):
            if dp[(sumt,i)] >= 0: 
                return dp[(sumt,i)]
            if i < n:
                b1 = dfs(sumt - nums[i],i + 1)
                b2 = dfs(sumt + nums[i],i + 1)
                dp[(sumt,i)] = b1 + b2
                return dp[(sumt,i)]
            elif sumt == target and i == n:
                dp[(sumt,i)] = 1
                return dp[(sumt,i)] 
            else:
                dp[(sumt,i)] = 0
                return dp[(sumt,i)] 
        return dfs(0,0)
                
