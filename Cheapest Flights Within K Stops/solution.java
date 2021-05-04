class Node
{
    int no;
    int cost;
    int level;
    public Node(int no,int cost,int level)
    {
        this.no = no;
        this.cost = cost;
        this.level = level;
    }
    public Node()
    {
    }
    public String toString()
    {
        return no+","+cost+","+level;
    }
}
class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int K) {
        K++;
        int ans = Integer.MAX_VALUE;
        Map<Integer,List<List<Integer>>> graph = new HashMap();
        for(int i=0;i<flights.length;i++)
        {
            Integer dest = flights[i][1];
            Integer price = flights[i][2];

            List<List<Integer>> cur = graph.getOrDefault(flights[i][0],new ArrayList());
            cur.add(Arrays.asList(dest,price));
            graph.put(flights[i][0],cur);
        }
        Comparator<Node> cmp = (Node p,Node q)->Integer.compare(p.cost,q.cost);
        Set<Integer> visited = new HashSet();
        PriorityQueue<Node> q = new PriorityQueue(cmp);
        q.add(new Node(src,0,0));
        visited.add(src);
        while(q.isEmpty() == false)
        {
            Node top = q.poll();
            int cur_node = top.no;
            int cur_cost = top.cost;
            int cur_level = top.level;
            if(cur_node == dst)
            {
                return cur_cost;
            }
            if(cur_level < K)
            {
                if(graph.containsKey(cur_node))
                {
                    for(List<Integer> child:graph.get(cur_node))
                    {

                        int next_node = child.get(0);
                        int cost = child.get(1);
                        if(visited.contains(next_node) == false)
                        {
                            Node child_node = new Node(next_node,cur_cost + cost,cur_level + 1);
                            q.add(child_node);
                        }

                    }
                }

            }


        }
        return -1;
    }
}