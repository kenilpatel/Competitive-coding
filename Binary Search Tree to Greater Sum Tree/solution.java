/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    Map<Integer,Integer> map;
    List<Integer> val;
    public TreeNode bstToGst(TreeNode root) {
        map = new HashMap<Integer,Integer>();
        val = new ArrayList<Integer>();
        int sum = 0;
        dfs(root);
        for(int i=val.size() - 1;i>=0;i--)
        {
            sum += val.get(i);

            map.put(val.get(i),sum);
        }
        // System.out.println(map);
        moddfs(root);
        return root;
    }
    public void dfs(TreeNode root)
    {
        if(root != null)
        {
            dfs(root.left);
            this.val.add(root.val);
            dfs(root.right);
        }
        return;
    }
    public void moddfs(TreeNode root)
    {
        if(root != null)
        {
            root.val = map.get(root.val);
            moddfs(root.left);
            moddfs(root.right);
        }
        return;
    }
}