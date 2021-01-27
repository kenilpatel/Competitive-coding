# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if  d == 1:
            return TreeNode(v,root,None)
        q = [(root,0)]
        while len(q) != 0:
            top,dt = q[0]
            if dt == d - 2:
                dr = top.right
                dl = top.left
                top.right = TreeNode(v,None,dr)
                top.left = TreeNode(v,dl,None)
            q = q[1:]
            if top.right != None and dt < d - 2:
                q.append((top.right,dt + 1))
            if top.left != None and dt < d - 2:
                q.append((top.left,dt + 1))
        return root
