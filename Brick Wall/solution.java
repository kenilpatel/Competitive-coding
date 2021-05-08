class Solution {
    public int leastBricks(List<List<Integer>> wall) {
        int n = wall.size();
        Map<Integer,Integer> edge_map = new HashMap();
        for(int i=0;i<n;i++)
        {
            int m = wall.get(i).size();
            List<Integer> wa = wall.get(i);
            int cur = 0;
            for(int j=0;j<m - 1;j++)
            {
                cur += wa.get(j);
                edge_map.put(cur,edge_map.getOrDefault(cur,0) + 1);
            }
        }
        int max = 0;
        for(Integer key:edge_map.keySet())
        {
            max = Math.max(max,edge_map.get(key));
        }
        return n - max;
    }
}