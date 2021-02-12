# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    cnt = 0

    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.cnt = 0
        if not root:
            return 0
        self.dfs(root, "")
        return self.cnt

    def dfs(self, root, parent):
        if not root:
            return True, parent
        else:
            bl, val_l = self.dfs(root.left, root.val)
            br, val_r = self.dfs(root.right, root.val)
            if bl and br:
                if val_l == val_r and val_l == root.val:
                    self.cnt += 1
                    return True, root.val
            return False, root.val
