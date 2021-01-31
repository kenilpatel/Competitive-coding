# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def get(self):
        return None

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dl1 = defaultdict(self.get)
        while l1.next != None:
            dl1[l1.next] = l1
            l1 = l1.next
        dl2 = defaultdict(self.get)
        while l2.next != None:
            dl2[l2.next] = l2
            l2 = l2.next
        v = 0
        ans = []
        while l1 != None and l2 != None:
            s = l1.val + l2.val + v
            if s > 9:
                v = 1
            else:
                v = 0
            s = s % 10
            ans.append(s)
            l1 = dl1[l1]
            l2 = dl2[l2]
        if l1 != None:
            while l1 != None:
                s = l1.val + v
                if s > 9:
                    v = 1
                else:
                    v = 0
                s = s % 10
                ans.append(s)
                l1 = dl1[l1]
        if l2 != None:
            while l2 != None:
                s = l2.val + v
                if s > 9:
                    v = 1
                else:
                    v = 0
                s = s % 10
                ans.append(s)
                l2 = dl2[l2]
        if v == 1:
            ans.append(v)
        ans = ans[::-1]
        dl3 = defaultdict(self.get)
        nextl = None
        ans_l = ListNode(ans[0])
        for i in range(1, len(ans)):
            nextl = ListNode(ans[i])
            ans_l.next = nextl
            dl3[nextl] = ans_l
            ans_l = nextl
            nextl = None
        while dl3[ans_l] != None:
            ans_l = dl3[ans_l]
        return ans_l
