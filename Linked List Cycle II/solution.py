# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tortoise = head
        hair = head
        while hair:
            try:
                tortoise = tortoise.next
                hair = hair.next.next
                if hair == tortoise:
                    break
            except:
                return None
        if hair == None:
            return None
        tortoise = head
        pos = 0 
        while tortoise != hair:
            tortoise = tortoise.next
            hair = hair.next 
        return tortoise
        
        
            
