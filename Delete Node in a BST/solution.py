# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root != None:
            queue = [(root, None)]
        else:
            queue = []
        while(len(queue) != 0):
            curr, parent = queue[0]
            queue = queue[1:]
            if curr.val == key:
                right = curr.right
                left = curr.left
                if right != None:
                    right_l = right.left
                    right_r = right.right
                    if right_l == None:
                        right.left = left
                    else:
                        while(right_l.left != None):
                            right_l = right_l.left
                        right_l.left = left
                    if parent != None:
                        if parent.right != None:
                            if parent.right.val == key:
                                parent.right = right
                            else:
                                parent.left = right
                        else:
                            parent.left = right
                    else:
                        root = right
                else:
                    if parent != None:
                        if parent.right != None:
                            if parent.right.val == key:
                                parent.right = left
                            else:
                                parent.left = left
                        else:
                            parent.left = left
                    else:
                        root = left
            else:
                if curr.left != None:
                    queue = queue + [(curr.left, curr)]
                if curr.right != None:
                    queue = queue + [(curr.right, curr)]
        return root
