class Solution {
    public boolean canReach(int[] arr, int start) {
        Set<Integer> end = new HashSet();
        int n = arr.length;
        for(int i=0;i<n;i++)
        {
            if(arr[i] == 0)
            {
                end.add(i);
            }
        }
        Deque<Integer> q = new ArrayDeque();
        Set<Integer> visited = new HashSet();
        q.addLast(start);
        while(q.isEmpty() == false)
        {
            int top = q.pollFirst();
            if(end.contains(top))
            {
                return true;
            }
            else
            {
                if(top + arr[top] < n)
                {
                    if(visited.contains(top + arr[top]) == false)
                    {
                        visited.add(top + arr[top]);
                        q.addLast(top + arr[top]);
                    }
                }
                if(top - arr[top] >= 0)
                {
                    if(visited.contains(top - arr[top]) == false)
                    {
                        visited.add(top - arr[top]);
                        q.addLast(top - arr[top]);
                    }
                }
            }
        }
        return false;
    }
}