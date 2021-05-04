class Solution {
    public int revInt(int num)
    {
        StringBuilder num_s = new StringBuilder(String.valueOf(num));
        num_s = num_s.reverse();
        return Integer.parseInt(num_s.toString());
    }
    public int countNicePairs(int[] nums) {
        Map<Integer,Integer> cmap = new HashMap();
        int MOD = 1000000007;
        int ans = 0;
        for(int i=0;i<nums.length;i++)
        {
            int key = nums[i] - revInt(nums[i]);
            int val = cmap.getOrDefault(key,0);
            ans += val;
            ans %= MOD;
            cmap.put(key, val + 1);
        }
        return ans % MOD;
    }
}