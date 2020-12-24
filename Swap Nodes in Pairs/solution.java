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
    public ListNode swapPairs(ListNode head) {
        if(head == null)
        {
            return null;
        }
        ListNode start = head;
        ListNode new_head;
        if(head.next != null)
            new_head = head.next;
        else
            new_head = head;
        while(true)
        {
            if(start.next!=null)
            {
                ListNode link = start.next.next;
                start.next.next = start;
                start.next = link;
            }
            ListNode new_start = start.next;
            if(new_start!=null)
            {
                if(new_start.next!=null)
                    start.next = new_start.next;
                else
                    start.next = new_start;
                start = new_start;
            }
            else
            {
                break;
            }
        }
        return new_head;
    }
}