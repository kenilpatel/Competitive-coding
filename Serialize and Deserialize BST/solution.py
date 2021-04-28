# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        def dfs(root):
            if root:
                ans.append(str(root.val))
                dfs(root.left)
                dfs(root.right)
        dfs(root) 
        return ",".join(ans)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # print(data)
        if data == "":
            return None
        ans = data.split(',')
        ans = [int(i) for i in ans] 
        def dfs(ans):
            n = len(ans)
            if n == 1:
                return TreeNode(ans[0])
            elif n == 0:
                return None
            else:
                root = TreeNode(ans[0])
                found = False
                for i,ele in enumerate(ans):
                    if ele > root.val:
                        found = True
                        break 
                if found == True:
                    left = ans[1:i]
                    right = ans[i:] 
                    # print(left)
                    # print(right)
                    root.left = dfs(left)
                    root.right = dfs(right)
                else:
                    root.left = dfs(ans[1:])
                    root.right = None
            return root
        return dfs(ans)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
