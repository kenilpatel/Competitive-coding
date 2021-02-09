# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    mapv = {}

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root
        nums = self.dfs(root)
        presum = []
        ans = 0
        for i in nums[::-1]:
            ans += i
            presum.append(ans)
        presum = presum[::-1]
        for i in range(0, len(nums)):
            self.mapv[nums[i]] = presum[i]
        self.dfschangeval(root)
        return root

    def dfschangeval(self, root):
        if root == None:
            return
        root.val = self.mapv[root.val]
        self.dfschangeval(root.left)
        self.dfschangeval(root.right)

    def dfs(self, root):
        if root != None:
            ans = []
            if root.left != None:
                ans += self.dfs(root.left)
            ans += [root.val]
            if root.right != None:
                ans += self.dfs(root.right)
            return ans
