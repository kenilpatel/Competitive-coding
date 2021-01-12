import math
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = None
        extra = 0
        head = None
        while l1 != None and l2 != None:
            val = l1.val + l2.val + extra
            if val == val % 10:
                extra = 0
            else:
                extra = 1
                val = val % 10
            if l3 == None:
                l3 = ListNode(val)
                head = l3
            else:
                l3.next = ListNode(val)
                l3 = l3.next
            l1 = l1.next
            l2 = l2.next
        if l1 != None:
            while l1 != None:
                val = l1.val + extra
                if val == val % 10:
                    extra = 0
                else:
                    extra = 1
                    val = val % 10
                if l3 == None:
                    l3 = ListNode(val)
                    head = l3
                else:
                    l3.next = ListNode(val)
                    l3 = l3.next
                l1 = l1.next
        if l2 != None:
            while l2 != None:
                val = l2.val + extra
                if val == val % 10:
                    extra = 0
                else:
                    extra = 1
                    val = val % 10
                if l3 == None:
                    l3 = ListNode(val)
                    head = l3
                else:
                    l3.next = ListNode(val)
                    l3 = l3.next
                l2 = l2.next
        if extra == 1:
            if l3 == None:
                l3 = ListNode(1)
                head = l3
            else:
                l3.next = ListNode(1)
                l3 = l3.next
        return head
