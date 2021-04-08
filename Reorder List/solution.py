# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        ptr = head 
        stack = [] 
        while ptr:
            stack.append(ptr)
            ptr = ptr.next

        ptr = head
        while True: 
            last = stack.pop()
            if ptr == last:
                break
            if ptr.next == ptr:
                break 
            last.next = ptr.next
            ptr.next = last
            ptr = last.next
        ptr.next = None
        return head
