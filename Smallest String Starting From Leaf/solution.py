# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    small = ""
    word = {}

    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """

        char = "a"
        for i in range(0, 26):
            self.word[i] = char
            char = chr(ord(char) + 1)
        self.dfs(root, "")
        return self.small

    def dfs(self, root, string):
        string = string + self.word[root.val]
        if(root.left == None):
            if(root.right == None):
                if self.small == "":
                    self.small = string[::-1]
                else:
                    # print(string[::-1], self.small)
                    if string[::-1] < self.small:
                        self.small = string[::-1]
            else:
                self.dfs(root.right, string)
        else:
            self.dfs(root.left, string)
            if(root.right != None):
                self.dfs(root.right, string)
