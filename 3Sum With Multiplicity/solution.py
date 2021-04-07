class Solution(object):
    def threeSumMulti(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)
        arr = sorted(arr)
        ans = 0
        cnt = defaultdict(lambda:0)
        for i in arr:
            cnt[i] += 1
        for i in range(0,n - 2):
            j = i + 1
            k = n - 1
            find = target - arr[i] 
            cnt[arr[i]] -= 1  
            while j < k:
                sumt = arr[j] + arr[k] 
                if sumt > find:
                    k -= 1
                elif sumt < find:
                    j += 1
                else:
                    if arr[j] != arr[k]:
                        ans += cnt[arr[j]] * cnt[arr[k]]
                    else:
                        ans += cnt[arr[j]] * (cnt[arr[j]] - 1) / 2
                    cmp1 = arr[j]
                    while j < n and arr[j] == cmp1:
                        j += 1
                    cmp2 = arr[k]
                    while k >= 0 and arr[k] == cmp2:
                        k -= 1 
        return ans % 1000000007
                    
                
