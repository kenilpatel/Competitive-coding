# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        parent_link = defaultdict(lambda:None)
        self.dep_l = 0
        level = defaultdict(lambda:[])
        def dfs(root,parent,l):
            if root:
                self.dep_l = max(self.dep_l,l)
                level[l].append(root)
                parent_link[root] = parent
                dfs(root.left,root,l + 1)
                dfs(root.right,root,l + 1) 
        dfs(root,None,0) 
        if len(level[self.dep_l]) == 1:
            return level[self.dep_l][0]
        else: 
            q = []
            n = len(level[self.dep_l])
            visited = defaultdict(lambda:0)
            for i in level[self.dep_l]:
                q.append(i)
                
            while q:
                top = q.pop(0)
                visited[top] += 1
                if visited[top] == n:
                    return top
                else:
                    parent = parent_link[top]   
                    q.append(parent)

                
            
