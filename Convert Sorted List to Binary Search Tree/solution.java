/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
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
import static java.lang.System.out;
class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        return generateTree(head);
    }
    public TreeNode generateTree(ListNode head)
    {
        if(head == null)
        {
            return null;
        }
        ListNode slow = head;
        ListNode fast = head;
        ListNode prev = null;
        while(fast.next != null && fast.next.next != null)
        {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        TreeNode root = new TreeNode();
        root.val = slow.val;
        slow = slow.next;
        if(prev == null)
        {
            root.left = null;
        }
        else
        {
            prev.next = null;
            root.left = generateTree(head);
        }
        if(slow == null)
        {
            root.right = null;
        }
        else
        {
            root.right = generateTree(slow);
        }
        return root;
    }

}