# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """ 
        def dfs(nums):
            maxn = max(nums)
            idx = nums.index(maxn)
            left = nums[0:idx]
            right = nums[idx + 1:]   
            ll = len(left)
            lr = len(right)
            root = TreeNode(maxn) 
            if ll > 1:
                root.left = dfs(left)
            elif ll == 1:
                root.left = TreeNode(left[0])
            if lr > 1:
                root.right = dfs(right)
            elif lr == 1:
                root.right = TreeNode(right[0])
            return root
        return dfs(nums)
            
