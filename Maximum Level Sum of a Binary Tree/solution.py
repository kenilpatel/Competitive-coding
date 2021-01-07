# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def getval(self):
        return 0

    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [(root, 1)]
        level_sum = defaultdict(self.getval)
        while len(queue) != 0:
            top, level = queue[0]
            level_sum[level] = level_sum[level] + top.val
            queue = queue[1:]
            if top.left != None:
                queue = queue + [(top.left, level + 1)]
            if top.right != None:
                queue = queue + [(top.right, level + 1)]
        max_sum = level_sum[1]
        max_level = 1
        for k in level_sum.keys():
            if max_sum < level_sum[k]:
                max_sum = level_sum[k]
                max_level = k
        return max_level
