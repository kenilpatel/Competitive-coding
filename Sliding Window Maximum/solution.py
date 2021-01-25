class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        de = []
        last = 0
        wm = []
        for i in range(0, len(nums)):
            while True:
                if len(de) == 0:
                    break
                top = de.pop()
                if nums[top] > nums[i]:
                    de.append(top)
                    break
            de.append(i)
            if i + 1 >= k:
                if de[0] == last:
                    wm.append(nums[de[0]])
                    de = de[1:]
                    last += 1
                    continue
                wm.append(nums[de[0]])
                last += 1
        return wm
