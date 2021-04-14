# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: TreeNode
        :type limit: int
        :rtype: TreeNode
        """ 
        back_path = defaultdict(lambda:0)
        parent_link = defaultdict(lambda:None)
        remove = set()
        def dfs(root,sumn):
            if root != None:
                left = float('-inf')
                right = float('-inf') 
                if root.left:
                    left = dfs(root.left,root.val)
                if root.right:
                    right = dfs(root.right,root.val)
                maxc = max(right,left)
                if maxc != float('-inf'):
                    back_path[root] = maxc 
                return root.val + back_path[root] 
        
        def fdfs(root,parent,sumn):
            if root:
                parent_link[root] = parent
                sumn += root.val
                if sumn + back_path[root] < limit:
                    remove.add(root)
                fdfs(root.left,root,sumn)
                fdfs(root.right,root,sumn)
        dfs(root,0)
        fdfs(root,None,0) 
        if root in remove:
            return None
        else:
            for i in remove:
                p = parent_link[i]
                if p.left == i:
                    p.left = None
                elif p.right == i:
                    p.right = None
            return root
                
                    
                    
                
