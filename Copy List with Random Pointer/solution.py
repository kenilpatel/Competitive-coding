"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """ 
        if head == None:
            return None
        ptr1 = head
        ptr2 = Node(head.val)
        ans = ptr2
        val_hash = defaultdict(lambda:None)
        next_val = float('inf')
        if head.next != None:
            next_val = head.next.val
        val_hash[head] = ptr2
        while ptr1: 
            next_val = float('inf')
            random_val = float('inf')
            if ptr1.next != None:
                next_val = ptr1.next.val
            if ptr1.random != None:
                random_val = ptr1.random.val 
            if next_val != float('inf'): 
                present_next = val_hash[ptr1.next] 
                if present_next == None:
                    present_next = Node(next_val)
                    val_hash[ptr1.next] = present_next
                ptr2.next = present_next
            if random_val != float('inf'): 
                random_next = val_hash[ptr1.random]
                if random_next == None:
                    random_next = Node(random_val)
                    val_hash[ptr1.random] = random_next
                ptr2.random = random_next
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ans
