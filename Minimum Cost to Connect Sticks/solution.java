class Solution {
    public int connectSticks(int[] sticks) {
        PriorityQueue < Integer > q = new PriorityQueue < Integer > ()
        int cost = 0
        for(int i=0
            i < sticks.length
            i++)
        {
            q.add(sticks[i])
        }
        while(true)
        {
            if(q.size() == 1)
            {
                return cost
            }
            int x = q.poll()
            int y = q.poll()
            cost += x + y
            q.add(x + y)
        }
    }
}
