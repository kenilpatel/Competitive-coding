class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(x,y):
            num1 = int(str(x) + str(y))
            num2 = int(str(y) + str(x))
            if num1 < num2:
                return -1
            elif num1 == num2:
                return 0
            else:
                return 1
        nums = sorted(nums,cmp = compare,reverse = True)
        ans = ""
        for i in nums:
            ans += str(i)
        return str(int(ans))
