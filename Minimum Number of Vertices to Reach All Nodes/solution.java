class Solution {
    public List<Integer> findSmallestSetOfVertices(int n, List<List<Integer>> edges) {
        Map<Integer,Integer> indegree = new HashMap();
        List<Integer> ans = new ArrayList();
        for(List<Integer> edge:edges)
        {
            int from = edge.get(0);
            int to = edge.get(1);
            indegree.put(to,indegree.getOrDefault(to,0) + 1);
        }
        for(int i=0;i<n;i++)
        {
            if(indegree.getOrDefault(i,0) == 0)
            {
                ans.add(i);
            }
        }
        return ans;
    }
}