class Solution {
    public boolean possibleBipartition(int N, int[][] dislikes) {
        boolean visited[] = new boolean[N + 1];
        int colors[] = new int[N + 1];
        Map<Integer,Set<Integer>> graph = new HashMap();
        for(int i=0;i<dislikes.length;i++)
        {
            int u = dislikes[i][0];
            int v = dislikes[i][1];
            Set<Integer> u_list = graph.getOrDefault(u,new HashSet<Integer>());
            Set<Integer> v_list = graph.getOrDefault(v,new HashSet<Integer>());
            u_list.add(v);
            v_list.add(u);
            graph.put(u,u_list);
            graph.put(v,v_list);
        }

        for(int i=1;i<N;i++)
        {
            Deque<Integer> q = new ArrayDeque();
            if(visited[i] == false)
            {
                visited[i] = true;
                colors[i] = 1;
                q.addLast(i);
                while(q.isEmpty() == false)
                {
                    int top = q.pollFirst();
                    int col = colors[top];
                    for(Integer child:graph.getOrDefault(top,new HashSet<Integer>()))
                    {
                        if(visited[child] == true)
                        {
                            if(colors[child] == colors[top])
                            {
                                return false;
                            }
                        }
                        else
                        {
                            q.addLast(child);
                            visited[child] = true;
                            if(col == 1)
                            {
                                colors[child] = 2;
                            }
                            else
                            {
                                colors[child] = 1;
                            }
                        }
                    }
                }
            }
        }
        return true;
    }
}