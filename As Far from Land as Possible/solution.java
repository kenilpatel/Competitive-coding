class Solution {
    int n;
    int m;
    public List<List<Integer>> getMove(int i,int j)
    {
        return Arrays.asList(Arrays.asList(i,j + 1),
                            Arrays.asList(i + 1,j),
                            Arrays.asList(i - 1,j),
                            Arrays.asList(i,j - 1));
    }
    public int maxDistance(int[][] grid) {
        Deque<List<Integer>> q = new ArrayDeque();
        Deque<Integer> d = new ArrayDeque();
        Set<List<Integer>> visited = new HashSet();
        n = grid.length;
        m = grid[0].length;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(grid[i][j] == 1)
                {
                    q.addLast(Arrays.asList(i,j));
                    d.addLast(0);
                    visited.add(Arrays.asList(i,j));
                }
            }
        }
        int ans = -1;
        while(q.isEmpty() == false)
        {
            List<Integer> top = q.pollFirst();
            int x = top.get(0);
            int y = top.get(1);
            int dist = d.pollFirst();
            if(grid[x][y] == 0)
            {
                ans = Math.max(ans,dist);
            }
            for(List<Integer> child:getMove(x,y))
            {
                int nx = child.get(0);
                int ny = child.get(1);
                if(nx >= 0 && nx < n && ny >= 0 && ny < m)
                {
                    if(visited.contains(child) == false)
                    {
                        visited.add(child);
                        q.addLast(child);
                        d.addLast(dist + 1);
                    }
                }
            }
        }
        return ans;
    }
}