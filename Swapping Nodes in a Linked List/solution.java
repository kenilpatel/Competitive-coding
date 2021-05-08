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
class Solution {
    public ListNode swapNodes(ListNode head, int k) {
        int i = 1;
        int n = 0;
        ListNode node = head;
        ListNode knode = null;
        ListNode lknode = null;
        while(node != null)
        {
            if(i == k)
            {
                knode = node;
            }
            i++;
            n++;
            node = node.next;
        }
        int nk = n - k + 1;
        i = 1;
        node = head;
        if(k == nk)
        {
            return head;
        }
        while(node != null)
        {
            if(i == nk)
            {
                lknode = node;
            }
            i++;
            node = node.next;
        }
        int temp = knode.val;
        knode.val = lknode.val;
        lknode.val = temp;
        return head;

    }
}