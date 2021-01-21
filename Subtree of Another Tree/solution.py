# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        root = None
        val = t.val
        queue = [s]
        ans = False
        while len(queue) != 0:
            top = queue[0]
            queue = queue[1:]
            if top.val == val:
                root = top
                ans = self.compare(root, t)
                if ans == True:
                    return True
            if top.left != None:
                queue.append(top.left)
            if top.right != None:
                queue.append(top.right)
        return False

    def compare(self, root, t):
        if root == None and t == None:
            return True
        if root == None and t != None:
            return False
        if root != None and t == None:
            return False
        if root.val != t.val:
            return False
        if root.val == t.val:
            return self.compare(root.left, t.left) and self.compare(root.right, t.right)
