class Solution {
    public int orderOfLargestPlusSign(int N, int[][] mines) {
        int right[][] = new int[N][N];
        int left[][] = new int[N][N];
        int up[][] = new int[N][N];
        int down[][] = new int[N][N];
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<N;j++)
            {
                right[i][j] = 1;
            }
        }
        for(int i=0;i<mines.length;i++)
        {
            int x = mines[i][0];
            int y = mines[i][1];
            right[x][y] = 0;
        }
        // left prefix sum
        for(int i=0;i<N;i++)
        {
            int sum = 0;
            for(int j=0;j<N;j++)
            {
                if(right[i][j] == 0)
                {
                    sum = 0;
                }
                else
                {
                    sum++;
                }
                left[i][j] = sum;
            }
        }
        // down prefix sum
        for(int j=0;j<N;j++)
        {
            int sum = 0;
            for(int i=0;i<N;i++)
            {
                if(right[i][j] == 0)
                {
                    sum = 0;
                }
                else
                {
                    sum++;
                }
                down[i][j] = sum;
            }
        }
        // up prefix sum
        for(int j=0;j<N;j++)
        {
            int sum = 0;
            for(int i=N-1;i>=0;i--)
            {
                if(right[i][j] == 0)
                {
                    sum = 0;
                }
                else
                {
                    sum++;
                }
                up[i][j] = sum;
            }
        }
        // right prefix sum
        for(int i=0;i<N;i++)
        {
            int sum = 0;
            for(int j=N-1;j>=0;j--)
            {
                if(right[i][j] == 0)
                {
                    sum = 0;
                }
                else
                {
                    sum++;
                }
                right[i][j] = sum;
            }
        }
        int ans = 0;
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<N;j++)
            {
                int pos = Collections.min(Arrays.asList(right[i][j],
                              left[i][j],
                              up[i][j],
                              down[i][j]));
                ans = Math.max(ans,pos);
            }
        }
        return ans;
    }
}