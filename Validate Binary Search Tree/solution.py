# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root, [], [])

    def dfs(self, root, right, left):
        if root == None:
            return True
        else:
            # print(root.val,"g",left,right)
            for v in right:
                if root.val <= v:
                    return False
            for v in left:
                if root.val >= v:
                    return False
            if root.left == None:
                if root.right == None:
                    return True
                else:
                    if root.val < root.right.val:
                        return self.dfs(root.right, right + [root.val], left)
                    else:
                        return False
            else:
                if root.right == None:
                    if root.val > root.left.val:
                        return self.dfs(root.left, right, left + [root.val])
                    else:
                        return False
                else:
                    if root.val > root.left.val and root.val < root.right.val:
                        return self.dfs(root.right, right + [root.val], left) and self.dfs(root.left, right, left + [root.val])
                    else:
                        return False
