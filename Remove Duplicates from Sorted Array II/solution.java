class Solution {
    public int removeDuplicates(int[] nums) {
        int count = 1;
        int prev = nums[0];
        int n = nums.length;
        for(int i=1;i<n;i++)
        {
            if(prev == nums[i])
            {
                count++;
                if(count > 2)
                {
                    nums[i] = Integer.MAX_VALUE;
                }
            }
            else
            {
                prev = nums[i];
                count = 1;
            }
        }
        int last = n - 1;
        for(int i=n - 1;i>=0;i--)
        {
            if(nums[i] == Integer.MAX_VALUE)
            {
                for(int j=i;j<last;j++)
                {
                    nums[j] = nums[j + 1];
                }
                nums[last] = Integer.MAX_VALUE;
                last--;
            }
        }
        int i=0;
        for(i=0;i<n;i++)
        {
            if(nums[i] == Integer.MAX_VALUE)
            {
                break;
            }
        }
        return i;

    }
}