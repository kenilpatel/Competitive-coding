"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    levle = None

    def get(self):
        return []

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        self.level = defaultdict(self.get)
        self.dfs(root, 0)
        for key in self.level.keys():
            nodes = self.level[key]
            for i in range(0, len(nodes) - 1):
                nodes[i].next = nodes[i + 1]
        return root

    def dfs(self, root, lvl):
        if root == None:
            return
        self.level[lvl].append(root)
        self.dfs(root.left, lvl + 1)
        self.dfs(root.right, lvl + 1)
