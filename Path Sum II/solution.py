# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        self.ans = []
        def dfs(root,path,spath): 
            if root:
                if root.right == None and root.left == None:
                    if spath + root.val == targetSum:
                        self.ans.append(path + [root.val])
                dfs(root.right,path + [root.val],spath + root.val)
                dfs(root.left,path + [root.val],spath + root.val)
        dfs(root,[],0) 
        return self.ans
