# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        fringe = [(root, [(root, 0)], 0)]
        pl = 0
        panl = []
        boop = False
        booq = False
        while len(fringe) != 0:
            top, anl, level = fringe.pop(0)
            if top.val == p.val:
                pl = level
                panl = anl
                boop = True
            if top.val == q.val:
                ql = level
                qanl = anl
                booq = True
            if boop == True and booq == True:
                break
            if top.left != None:
                if top.left.val == p.val:
                    pl = level + 1
                    panl = anl + [(top.left, level + 1)]
                    boop = True
                if top.left.val == q.val:
                    ql = level + 1
                    qanl = anl + [(top.left, level + 1)]
                    booq = True
                if boop == True and booq == True:
                    break
                fringe.append(
                    (top.left, anl + [(top.left, level + 1)], level + 1))
            if top.right != None:
                if top.right.val == p.val:
                    pl = level + 1
                    panl = anl + [(top.right, level + 1)]
                    boop = True
                if top.right.val == q.val:
                    ql = level + 1
                    qanl = anl + [(top.right, level + 1)]
                    booq = True
                if boop == True and booq == True:
                    break
                fringe.append(
                    (top.right, anl + [(top.right, level + 1)], level + 1))
        qd = {}
        pd = {}
        for en in qanl:
            qd[en[1]] = en[0]
        for en in panl:
            pd[en[1]] = en[0]
        for j in range(min(pl, ql), -1, -1):
            if pd[j].val == qd[j].val:
                return pd[j]
