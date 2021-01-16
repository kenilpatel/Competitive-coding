import math
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        tot = len1 + len2
        index = -1
        i = 0
        j = 0
        if (tot - 1) % 2 == 0:
            int1 = (tot - 1) / 2
            int2 = (tot - 1) / 2
        else:
            int1 = int(math.floor((tot - 1) / 2))
            int2 = int1 + 1
        num1 = None
        num2 = None
        while i < len1 and j < len2:
            index += 1
            # print(index,i,j)
            if nums1[i] <= nums2[j]:
                if index == int1:
                    num1 = nums1[i]
                if index == int2:
                    num2 = nums1[i]
                i += 1
            else:
                if index == int1:
                    num1 = nums2[j]
                if index == int2:
                    num2 = nums2[j]
                j += 1
            if num1 != None and num2 != None:
                return float((num1 + num2) / 2.0)
        if i < len1:
            while i < len1:
                index += 1
                if index == int1:
                    num1 = nums1[i]
                if index == int2:
                    num2 = nums1[i]
                i += 1
                if num1 != None and num2 != None:
                    return float((num1 + num2) / 2.0)
        if j < len2:
            while j < len2:
                index += 1
                if index == int1:
                    num1 = nums2[j]
                if index == int2:
                    num2 = nums2[j]
                j += 1
                if num1 != None and num2 != None:
                    return float((num1 + num2) / 2.0)