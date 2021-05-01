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
    public boolean isUnivalTree(TreeNode root) {
        if(root == null)
        {
            return true;
        }
        else
        {
            return check(root,root.val);
        }
    }
    public boolean check(TreeNode root,int val)
    {
        boolean ans = root.val == val;
        if(ans == false)
        {
            return false;
        }
        if(root.left != null)
        {
            ans = ans & check(root.left,val);
            if(ans == false)
            {
                return false;
            }
        }
        if(root.right != null)
        {
            ans = ans & check(root.right,val);
            if(ans == false)
            {
                return false;
            }
        }
        return true;
    }
}