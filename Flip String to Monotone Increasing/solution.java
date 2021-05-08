class Solution {
    public int minFlipsMonoIncr(String S) {
        int n = S.length();
        int pre_zero[] = new int[n];
        int post_one[] = new int[n];
        for(int i=0;i<n;i++)
        {
            pre_zero[i] = S.charAt(i) == '1' ? 0:1;
            if(i - 1 >= 0)
            {
                pre_zero[i] += pre_zero[i - 1];
            }
        }
        for(int i=n - 1;i>=0;i--)
        {
            post_one[i] = S.charAt(i) == '1' ? 1:0;
            if(i + 1 < n)
            {
                post_one[i] += post_one[i + 1];
            }
        }
        int ans = Integer.MAX_VALUE;
        for(int i=0;i<n-1;i++)
        {
            int zero = pre_zero[i];
            int one = post_one[i + 1];
            int size_zero = i + 1;
            int size_one = n - (i + 1);
            ans = Math.min(ans,size_zero - zero + size_one - one);
        }
        int tot_zero = pre_zero[n - 1];
        int tot_one = post_one[0];
        ans = Math.min(ans,n  - tot_zero);
        ans = Math.min(ans,n - tot_one);
        return ans;
    }
}