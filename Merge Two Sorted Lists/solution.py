# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head1 = copy.deepcopy(l1)
        head2 = copy.deepcopy(l2)
        merge = None
        merge_head = None
        while(head1 != None and head2 != None):
            if(head1.val <= head2.val):
                if merge == None:
                    merge = copy.deepcopy(head1)
                    merge_head = merge
                else:
                    merge.next = copy.deepcopy(head1)
                    merge = merge.next
                head1 = head1.next
            else:
                if merge == None:
                    merge = copy.deepcopy(head2)
                    merge_head = merge
                else:
                    merge.next = copy.deepcopy(head2)
                    merge = merge.next
                head2 = head2.next
        if head1 != None:
            while(head1 != None):
                if merge == None:
                    merge = copy.deepcopy(head1)
                    merge_head = merge
                else:
                    merge.next = copy.deepcopy(head1)
                    merge = merge.next
                head1 = head1.next
        if head2 != None:
            while(head2 != None):
                if merge == None:
                    merge = copy.deepcopy(head2)
                    merge_head = merge
                else:
                    merge.next = copy.deepcopy(head2)
                    merge = merge.next
                head2 = head2.next
        return merge_head
