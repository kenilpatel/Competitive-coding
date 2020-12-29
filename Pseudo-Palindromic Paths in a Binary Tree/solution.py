import copy
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    count = 0

    def pseudoPalindromicPaths(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root, {})
        return self.count

    def dfs(self, root, dict_count):
        if root.val in dict_count.keys():
            dict_count[root.val] = dict_count[root.val] + 1
        else:
            dict_count[root.val] = 1
        print(dict_count)
        if root.left == None and root.right == None:
            on = 0
            for key in dict_count.keys():
                if dict_count[key] % 2 == 1:
                    on = on + 1
                if on > 1:
                    return
            self.count = self.count + 1
        if root.left != None:
            self.dfs(root.left, copy.deepcopy(dict_count))
        if root.right != None:
            self.dfs(root.right, copy.deepcopy(dict_count))
        return
