class Solution {
    public List<List<Integer>> getMove(int i,int j)
    {
            return Arrays.asList(
                Arrays.asList(i,j + 1),
                Arrays.asList(i,j - 1),
                Arrays.asList(i + 1,j),
                Arrays.asList(i - 1,j)
            );
    }
    public int numEnclaves(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        int j,i;
        Deque<List<Integer>> q = new ArrayDeque();
        j = 0;
        for(i=0;i<n;i++)
        {
            if(grid[i][j] == 1)
            {
                grid[i][j] = -1;
                q.addLast(Arrays.asList(i,j));
            }
        }

        j = m-1;
        for(i=0;i<n;i++)
        {
            if(grid[i][j] == 1)
            {
                grid[i][j] = -1;
                q.addLast(Arrays.asList(i,j));
            }
        }


        i = 0;
        for(j=0;j<m;j++)
        {
            if(grid[i][j] == 1)
            {
                grid[i][j] = -1;
                q.addLast(Arrays.asList(i,j));
            }
        }

        i = n-1;
        for(j=0;j<m;j++)
        {
            if(grid[i][j] == 1)
            {
                grid[i][j] = -1;
                q.addLast(Arrays.asList(i,j));
            }
        }
        while(q.isEmpty() == false)
        {
            List<Integer> arr = q.pollFirst();
            int x = arr.get(0);
            int y = arr.get(1);
            for(List<Integer> next:getMove(x,y))
            {
                int nx = next.get(0);
                int ny = next.get(1);
                if(nx >= 0 && nx < n && ny >= 0 && ny < m)
                {
                    if(grid[nx][ny] == 1)
                    {
                        grid[nx][ny] = -1;
                        q.addLast(Arrays.asList(nx,ny));
                    }
                }
            }

        }
        int ans = 0;
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                if(grid[i][j] == 1)
                {
                    ans++;
                }
            }
        }
        return ans;
    }
}