class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        first = nums[0]
        last = nums[high]
        while low <= high:
            mid = (low + high) / 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[(mid + 1) % len(nums)]:
                break
            else:
                if nums[mid] >= first:
                    low = mid + 1
                else:
                    high = mid - 1
        part1 = nums[0:mid + 1]
        part2 = nums[mid + 1:]
        if target >= first and target <= nums[mid]:
            low = 0
            high = mid
            if len(part1) == 0:
                return -1
            while low <= high:
                m = (low + high) / 2
                if nums[m] == target:
                    return m
                else:
                    if nums[m] < target:
                        low = m + 1
                    else:
                        high = m - 1
            return -1
        else:
            low = mid + 1
            high = len(nums) - 1
            if len(part2) == 0:
                return -1
            while low <= high:
                m = (low + high) / 2
                if nums[m] == target:
                    return m
                else:
                    if nums[m] < target:
                        low = m + 1
                    else:
                        high = m - 1
            return -1
