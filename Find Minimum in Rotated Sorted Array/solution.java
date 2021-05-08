class Solution {
    public int findMin(int[] nums) {
        int first = nums[0];
        int low = 0;
        int n = nums.length;
        int high = n - 1;
        while(low <= high)
        {
            int mid = (int)Math.ceil((low + high) / 2.0);
            int left = mid - 1;
            if(left < 0)
            {
                left = n - 1;
            }
            int right = (mid + 1) % n;
            if(nums[mid] < nums[right] && nums[mid] < nums[left])
            {
                return nums[mid];
            }
            else if(nums[mid] > first)
            {
                low = mid + 1;
            }
            else
            {
                high = mid - 1;
            }
        }
        return Math.min(nums[0],nums[n - 1]);
    }
}