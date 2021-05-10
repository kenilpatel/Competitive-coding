class Node
{
    int id,level;
    public Node(int id,int level)
    {
        this.id = id;
        this.level = level;
    }
    public int hashCode()
    {
        return id;
    }
}
class Count implements Comparable<Count>
{
    int count;
    String str;
    public Count(int cc,String s)
    {
        str = s;
        count = cc;
    }
    public int compareTo(Count b)
    {
        if(this.count == b.count)
        {
            return this.str.compareTo(b.str);
        }
        else
        {
            return this.count - b.count;
        }
    }
    public String toString()
    {
        return str;
    }
}
class Solution {
    public List<String> watchedVideosByFriends(List<List<String>> watchedVideos, int[][] friends, int id, int level) {
        List<Integer> friend = new ArrayList();
        Deque<Node> q = new ArrayDeque();
        Set<Integer> visited = new HashSet();
        Node self = new Node(id,0);
        q.addLast(self);
        visited.add(self.id);
        while(q.isEmpty() == false)
        {
            Node top = q.pollFirst();
            if(top.level == level)
            {
                friend.add(top.id);
            }
            if(top.level + 1 <= level)
            {
                for(int i=0;i<friends[top.id].length;i++)
                {
                    Node child = new Node(friends[top.id][i],top.level + 1);
                    if(visited.contains(child.id) == false)
                    {
                        visited.add(child.id);
                        q.addLast(child);
                    }
                }
            }
        }
        System.out.println(friend);
        Map<String,Integer> count = new HashMap();
        for(Integer i:friend)
        {

            for(String movie:watchedVideos.get(i))
            {
                count.put(movie,count.getOrDefault(movie,0) + 1);
            }
        }
        List<Count> array = new ArrayList();
        for(String key:count.keySet())
        {
            array.add(new Count(count.get(key),key));
        }
        Collections.sort(array);
        List<String> ans = new ArrayList();
        for(Count a:array)
        {
            ans.add(a.str);
        }
        return ans;
    }
}