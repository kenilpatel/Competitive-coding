# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        ptr = head 
        n = 0
        while ptr:
            ptr = ptr.next   
            n += 1 
        itr = n - k % n
        prev = None
        ptr = head
        if itr == 0 or itr == n:
            return head
        print(itr)
        for _ in range(itr):
            prev = ptr
            ptr = ptr.next
        prev.next = None
        new_head = ptr
        while ptr.next != None:
            ptr = ptr.next
        ptr.next = head
        return new_head
