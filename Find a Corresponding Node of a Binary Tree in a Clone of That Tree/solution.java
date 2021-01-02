/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public final TreeNode getTargetCopy(final TreeNode original, final TreeNode cloned, final TreeNode target) {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        stack.push(cloned);
        while(!stack.empty())
        {
            TreeNode top = stack.pop();
            int val = 0;
            int right = 0;
            int left = 0;
            if(top.val == target.val)
            {
                val = 1;
            }
            if(val == 1)
            {
                if(top.left == null)
                {
                    if(target.left == null)
                    {
                        left = 1;
                    }
                }
                else
                {
                    if(top.left != null && target.left != null)
                    {
                        if(top.left.val == target.left.val)
                        {
                            left = 1;
                        }
                    }
                }
            }
            if(left == 1)
            {
                if(top.right == null)
                {
                    if(target.right == null)
                    {
                        right = 1;
                    }
                }
                else
                {
                    if(top.right != null && target.right != null)
                    {
                        if(top.right.val == target.right.val)
                        {
                            right = 1;
                        }
                    }
                }
            }
            if(right == 1 && left == 1 && val == 1)
            {
                return top;
            }
            if(top.left != null)
            {
                stack.push(top.left);
            }
            if(top.right != null)
            {
                stack.push(top.right);
            }
        }
        return null;
    }

}