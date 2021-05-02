class Solution {
    int ans[][];
    int cur_val;
    public int[][] generateMatrix(int n) {
        this.ans = new int[n][n];
        this.cur_val = 1;
        int si = 0;
        int sj = 0;
        int ei = n;
        int ej = n;
        int x = (int)Math.floor(n / 2.0);
        for(int ni=0;ni<x;ni++)
        {
            int i = si;
            int j = sj;
            for(j=sj;j<ej;j++)
            {
                this.ans[i][j] = this.cur_val;
                this.cur_val++;
            }
            this.cur_val--;
            j = ej - 1;
            for(i=si;i<ei;i++)
            {
                this.ans[i][j] = this.cur_val;
                this.cur_val++;
            }
            this.cur_val--;
            i = ei - 1;
            for(j=ej-1;j>=sj;j--)
            {
                this.ans[i][j] = this.cur_val;
                this.cur_val++;
            }
            this.cur_val--;
            j = sj;
            for(i=ei-1;i>=si + 1;i--)
            {
                this.ans[i][j] = this.cur_val;
                this.cur_val++;
            }
            si++;
            sj++;
            ei--;
            ej--;
        }

        if(n % 2 == 1)
        {
            ans[x][x] = this.cur_val;
        }
        return ans;
    }
}