class Solution {
    int n;
    int m;
    public List<List<Integer>> getMove(int i,int j)
    {
        return Arrays.asList(Arrays.asList(i + 1,j),
                            Arrays.asList(i - 1,j),
                            Arrays.asList(i,j + 1),
                            Arrays.asList(i,j - 1));
    }
    public boolean valid(int i,int j)
    {
        return i >= 0 && i < n && j >= 0 && j < m;
    }
    public int shortestBridge(int[][] A) {
        int id = 1;
        Set<List<Integer>> visited = new HashSet();
        n = A.length;
        m = A[0].length;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                List<Integer> cord = Arrays.asList(i,j);
                if(visited.contains(cord))
                {
                    continue;
                }
                else if(A[i][j] != 0)
                {
                    visited.add(cord);
                    Deque<List<Integer>> q = new ArrayDeque();
                    q.addLast(cord);
                    A[cord.get(0)][cord.get(1)] = id;
                    while(q.size()>0)
                    {
                        List<Integer> top = q.pollFirst();
                        A[top.get(0)][top.get(1)] = id;
                        for(List<Integer> child:getMove(top.get(0),top.get(1)))
                        {
                            if(child.get(0) >= 0 &
                               child.get(0) < n &
                               child.get(1) >= 0 &
                               child.get(1) < m)
                            {
                                if(visited.contains(child) == false &
                                   A[child.get(0)][child.get(1)] != 0)
                                {
                                    visited.add(child);
                                    q.addLast(child);
                                }
                            }

                        }
                    }
                    id += 1;
                }
            }
        }
        int dist = Integer.MAX_VALUE;
        Deque<List<Integer>> q = new ArrayDeque();
        Deque<Integer> d = new ArrayDeque();
        Set<List<Integer>> lv = new HashSet();
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(A[i][j] == 1)
                {
                    q.addLast(Arrays.asList(i,j));
                    d.addLast(0);
                    lv.add(Arrays.asList(i,j));
                }
            }
        }
        while(q.isEmpty() != true)
        {
            List<Integer> top = q.pollFirst();
            int topd = d.pollFirst();
            int x = top.get(0);
            int y = top.get(1);
            if(A[x][y] == 2)
            {
                return topd - 1;
            }
            for(List<Integer> child:getMove(x,y))
            {
                if(lv.contains(child) == false && valid(child.get(0),child.get(1)))
                {
                    q.addLast(child);
                    d.addLast(topd + 1);
                    lv.add(child);
                }
            }
        }
        return 0;
    }
}