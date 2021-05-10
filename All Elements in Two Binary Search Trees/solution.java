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
    List<Integer> one;
    List<Integer> two;
    public void dfs_one(TreeNode root)
    {
        if(root != null)
        {
            dfs_one(root.left);
            one.add(root.val);
            dfs_one(root.right);
        }
    }
    public void dfs_two(TreeNode root)
    {
        if(root != null)
        {
            dfs_two(root.left);
            two.add(root.val);
            dfs_two(root.right);
        }
    }
    public List<Integer> getAllElements(TreeNode root1, TreeNode root2) {
        one = new ArrayList();
        two = new ArrayList();
        dfs_one(root1);
        dfs_two(root2);
        List<Integer> ans = new ArrayList();
        int i=0;
        int j=0;
        int n = one.size();
        int m = two.size();
        while(i < n && j < m)
        {
            int a = one.get(i);
            int b = two.get(j);
            if(a <= b)
            {
                ans.add(a);
                i++;
            }
            else
            {
                ans.add(b);
                j++;
            }
        }
        while(i < n)
        {
            int a = one.get(i);
            ans.add(a);
            i++;
        }
        while(j < m)
        {
            int a = two.get(j);
            ans.add(a);
            j++;
        }
        return ans;
    }
}