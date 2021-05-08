class Solution {
    int[] nums;
    Set<List<Integer>> ans;
    int n;
    public List<List<Integer>> findSubsequences(int[] nums) {
        this.nums = nums;
        this.n = nums.length;
        ans = new HashSet();
        dfs(0,new ArrayList<Integer>(),0);
        return new ArrayList(ans);
    }
    public void dfs(int start,List<Integer> arr,int size)
    {
        if(size >= 2)
        {
            ans.add(arr);
        }
        for(int i=start;i<n;i++)
        {
            if(size == 0)
            {
                List<Integer> narr = new ArrayList(arr);
                narr.add(nums[i]);
                dfs(i + 1,narr,size + 1);
            }
            else
            {
                int last = arr.get(size - 1);
                if(nums[i] - last >= 0)
                {
                    List<Integer> narr = new ArrayList(arr);
                    narr.add(nums[i]);
                    dfs(i + 1,narr,size + 1);
                }
            }
        }
    }
}