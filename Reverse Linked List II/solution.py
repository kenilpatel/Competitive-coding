# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if head == None:
            return None
        previous = defaultdict(lambda:None)
        leftp = head
        rightp = head
        previous[head] = None
        for i in range(right - left):
            previous[rightp.next] = rightp
            rightp = rightp.next
        # print(leftp.val,rightp.val)
        i = 1
        while i != left: 
            previous[leftp.next] = leftp
            previous[rightp.next] = rightp
            leftp = leftp.next
            rightp = rightp.next
            i += 1 
        while left < right:
            leftp.val,rightp.val = rightp.val,leftp.val
            leftp = leftp.next
            rightp = previous[rightp]
            left += 1
            right -= 1
        return head
