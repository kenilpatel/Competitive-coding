class Solution(object):
    def get(self):
        return []

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        index = defaultdict(self.get)
        ans = set()
        for i in range(0, len(nums)):
            index[nums[i]].append(i)
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    s = target - nums[i] - nums[j] - nums[k]
                    for l in index[s]:
                        if l > k:
                            ans.add(
                                tuple(sorted((nums[i], nums[j], nums[k], s))))
        return ans
