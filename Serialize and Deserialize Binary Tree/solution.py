# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    leveld = None

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        q = [(root, 0)]
        ans = []
        self.leveld = defaultdict(lambda: [])
        while q:
            top, level = q.pop(0)
            if top != None:
                self.leveld[level].append(top.val)
                ans.append(top.val)
                q.append((top.left, level + 1))
                q.append((top.right, level + 1))
            else:
                self.leveld[level].append(None)
                ans.append(None)
        return self.leveld

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        leveld = dict(data)
        if leveld[0][0] != None:
            root = TreeNode(leveld[0][0])
            self.dfs(root, 0, leveld)
        else:
            root = None
        return root

    def dfs(self, root, level, leveld):
        if root != None and level + 1 in leveld.keys():
            x = leveld[level + 1].pop(0)
            y = leveld[level + 1].pop(0)
            if x != None:
                root.left = TreeNode(x)
                self.dfs(root.left, level + 1, leveld)
            if y != None:
                root.right = TreeNode(y)
                self.dfs(root.right, level + 1, leveld)
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
