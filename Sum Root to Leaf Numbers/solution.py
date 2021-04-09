# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def dfs(root,path):
            if root == None:
                return
            elif root.left == None and root.right == None: 
                self.ans += int(path + str(root.val))
            else:
                
                dfs(root.left,path + str(root.val))
                dfs(root.right,path + str(root.val))
        dfs(root,"")
        return self.ans
