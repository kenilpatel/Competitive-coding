# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def get(self):
        return []

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        level = defaultdict(self.get)
        queue = [(root, 0)]
        if root == None:
            return []
        while len(queue) != 0:
            top, depth = queue[0]
            if depth % 2 == 0:
                level[depth].append(top.val)
            else:
                level[depth].insert(0, top.val)
            queue = queue[1:]
            if top.left != None:
                queue.append((top.left, depth + 1))
            if top.right != None:
                queue.append((top.right, depth + 1))
        ans = []
        for l in level.values():
            ans.append(l)
        return ans
