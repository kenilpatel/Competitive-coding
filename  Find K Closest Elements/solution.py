class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        result = []
        idx = bisect.bisect_left(arr, x)
        if idx >= len(arr):
            high = idx - 1
            low = idx - 2
        elif idx - 1 >= 0 and abs(x - arr[idx - 1]) <= abs(x - arr[idx]):
            low = idx - 1
            high = idx
        elif idx + 1 < len(arr) and abs(x - arr[idx + 1]) <= abs(x - arr[idx]):
            low = idx + 1
            high = idx + 2
        else:
            low = idx
            high = idx + 1
        while low >= 0 and high < len(arr) and k != 0:
            if abs(arr[low] - x) <= abs(arr[high] - x):
                result.append(arr[low])
                low -= 1
            else:
                result.append(arr[high])
                high += 1
            k -= 1
        while low >= 0 and k != 0:
            result.append(arr[low])
            low -= 1
            k -= 1
        while high < len(arr) and k != 0:
            result.append(arr[high])
            high += 1
            k -= 1
        return sorted(result)
