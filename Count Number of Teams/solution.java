class Solution {
    public int numTeams(int[] rating) {
        int n = rating.length;
        int pre[] = new int[rating.length];
        int post[] = new int[rating.length];
        for(int i=1;i<n;i++)
        {
            int count=0;
            for(int j=0;j<i;j++)
            {
                if(rating[j] < rating[i])
                {
                    count++;
                }
            }
            pre[i] = count;
        }
        for(int i=0;i<n - 1;i++)
        {
            int count=0;
            for(int j=i + 1;j<n;j++)
            {
                if(rating[j] > rating[i])
                {
                    count++;
                }
            }
            post[i] = count;
        }
        int ans = 0;
        for(int i=1;i<n - 1;i++)
        {
            ans += pre[i] * post[i];
        }


        for(int i=1;i<n;i++)
        {
            int count=0;
            for(int j=0;j<i;j++)
            {
                if(rating[j] > rating[i])
                {
                    count++;
                }
            }
            pre[i] = count;
        }
        for(int i=0;i<n - 1;i++)
        {
            int count=0;
            for(int j=i + 1;j<n;j++)
            {
                if(rating[j] < rating[i])
                {
                    count++;
                }
            }
            post[i] = count;
        }
        for(int i=1;i<n - 1;i++)
        {
            ans += pre[i] * post[i];
        }
        return ans;
    }
}