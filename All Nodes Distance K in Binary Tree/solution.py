# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    graph = None

    def getlist(self):
        return []

    def getbool(self):
        return False

    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        self.graph = defaultdict(self.getlist)
        if target != None:
            self.dfs(root, None)
            queue = [(target, 0)]
            visited = defaultdict(self.getbool)
            visited[target] = True
            ans = []
            while len(queue) != 0:
                top, depth = queue[0]
                if depth == k:
                    ans.append(top.val)
                queue = queue[1:]
                for c in self.graph[top]:
                    if depth + 1 <= k:
                        if visited[c] == False:
                            visited[c] = True
                            queue.append((c, depth + 1))
            return ans
        else:
            return []

    def dfs(self, root, parent):
        if parent != None:
            self.graph[root].append(parent)
        if root.left != None:
            self.graph[root].append(root.left)
            self.dfs(root.left, root)
        if root.right != None:
            self.graph[root].append(root.right)
            self.dfs(root.right, root)
