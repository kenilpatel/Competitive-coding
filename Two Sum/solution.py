class Solution(object):
    def val(self):
        return []
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = defaultdict(self.val)
        for i in range(0,len(nums)):
            dict[nums[i]].append(i)
        for key in dict.keys():
            find = target - key
            if dict[find] != []:
                if key == find:
                    return [dict[key][0],dict[key][1]]
                return [dict[key][0],dict[find][0]]