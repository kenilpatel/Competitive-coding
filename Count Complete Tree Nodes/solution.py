# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.level = 0 
        def dfs_left(root):
            if root:
                self.level += 1
                dfs_left(root.left)
        dfs_left(root)
        self.tot_nodes = 0  
        for h in range(self.level):
            self.tot_nodes += 2 ** h 
        self.global_stop = False
        def dfs(root,cur_level): 
            if root == None: 
                if cur_level == self.level:  
                    self.tot_nodes -= 1
            elif root and cur_level == self.level:
                    self.global_stop = True
            elif not self.global_stop: 
                dfs(root.right,cur_level + 1)
                dfs(root.left,cur_level + 1)
        dfs(root,1)
        return self.tot_nodes      
                
