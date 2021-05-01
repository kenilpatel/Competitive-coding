/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {

    public List<List<Integer>> levelOrder(Node root) {
        Map<Integer,List<Node>> level_map = new HashMap<Integer,List<Node>>();
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        if(root == null)
        {
            return ans;
        }
        Deque<Integer> q1 = new ArrayDeque<Integer>();
        Deque<Node> q2 = new ArrayDeque<Node>();
        q1.addLast(0);
        q2.addLast(root);
        while(q1.size() > 0)
        {
            int level = q1.pollFirst();
            Node n = q2.pollFirst();
            List<Node> cur = level_map.getOrDefault(level,new ArrayList<Node>());
            cur.add(n);
            level_map.put(level,cur);
            for(Node child:n.children)
            {
                q1.addLast(level + 1);
                q2.addLast(child);
            }
        }
        for(Integer key:level_map.keySet())
        {
            List<Node> n_arr = level_map.get(key);
            List<Integer> local = new ArrayList<>();
            for(Node n:n_arr)
            {
                local.add(n.val);
            }
            ans.add(local);
        }
        return ans;
    }
}