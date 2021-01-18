# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def getlist(self):
        return []

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        level_d = defaultdict(self.getlist)
        if root == None:
            return []
        queue = [(root, 0)]
        while len(queue) != 0:
            top, level = queue[0]
            level_d[level].append(top.val)
            queue = queue[1:]
            if top.left != None:
                queue.append((top.left, level + 1))
            if top.right != None:
                queue.append((top.right, level + 1))
        ans = []
        for key in level_d:
            ans.append(level_d[key])
        return ans
