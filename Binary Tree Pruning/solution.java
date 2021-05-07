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
    TreeNode ans;
    public TreeNode pruneTree(TreeNode root) {
        ans = root;
        dfs(root,null);
        return ans;
    }
    public boolean dfs(TreeNode root,TreeNode parent)
    {
        if(root != null)
        {
            boolean x = root.val == 1 || dfs(root.left,root) || dfs(root.right,root);
            if(x == false)
            {
                if(parent == null)
                {
                    ans = null;
                }
                else
                {
                    if(parent.right == root)
                    {
                        parent.right = null;
                    }
                    else
                    {
                        parent.left = null;
                    }
                }
            }
            else
            {
                dfs(root.left,root);
                dfs(root.right,root);
            }
            return x;
        }
        else
        {
            return false;
        }
    }

}