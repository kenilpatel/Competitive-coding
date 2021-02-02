from collections import OrderedDict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        od = OrderedDict()
        q = [(root, 0)]
        while q:
            top, level = q.pop(0)
            od[level] = top.val
            if top.left != None:
                q.append((top.left, level + 1))
            if top.right != None:
                q.append((top.right, level + 1))
        return od.values()
