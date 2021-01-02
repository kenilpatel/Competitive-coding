class Solution {
    public int unhappyFriends(int n, int[][] preferences, int[][] pairs) {
        int rank_matrix[][] = new int[n][n];
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for(int i=0;i<preferences.length;i++)
        {
            for(int j=0;j<preferences[i].length;j++)
            {
                rank_matrix[i][preferences[i][j]] = n - j - 1;
            }
        }
        for(int i=0;i<pairs.length;i++)
        {
            int x = pairs[i][0];
            int y = pairs[i][1];
            map.put(x, rank_matrix[x][y]);
            map.put(y, rank_matrix[y][x]);
        }
        int uh = 0;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                int x = i;
                int y = j;
                int current_x = map.get(x);
                int current_y = map.get(y);
                if(rank_matrix[x][y]>current_x && rank_matrix[y][x]>current_y)
                {
                    uh = uh + 1;
                    break;
                }
            }
        }
        return uh;
    }
}