class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder = preorder.split(',')
        stack = []
        if preorder[0] != "#":
            stack.append([preorder[0],0])
        for i in preorder[1:]:
            if stack:
                top = stack.pop()
            else:
                return False
            top[1] += 1
            stack.append(top) 
            if i != '#':
                stack.append([i,0])
            else:  
                if stack:
                    while stack and stack[-1][1] == 2:
                        stack.pop() 
                else:
                    return False
        return len(stack) == 0
            
            
