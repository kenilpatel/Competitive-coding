# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        level_d = defaultdict(lambda: [])
        level_none = defaultdict(lambda: 0)
        q = [(root, 0)]
        last_level = 0
        while q:
            top, level = q.pop(0)
            last_level = level
            if top != None:
                level_d[level].append(top.val)
                right = top.right
                left = top.left
                q.append((left, level + 1))
                q.append((right, level + 1))
            else:
                level_none[level] += 1
                level_d[level].append(None)
        last_level -= 1
        for i in range(0, last_level):
            if level_none[i] != 0:
                return False
        none_t = False
        for child in level_d[last_level]:
            if child == None:
                none_t = True
            if none_t == True:
                if child != None:
                    return False
        return True
