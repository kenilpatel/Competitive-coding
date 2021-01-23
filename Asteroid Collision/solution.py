class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for i in asteroids:
            ins = i
            if len(stack) == 0:
                stack.insert(0, ins)
                continue
            if stack[0] > 0 and ins > 0:
                stack.insert(0, ins)
                continue
            if stack[0] < 0 and ins < 0:
                stack.insert(0, ins)
                continue
            if stack[0] < 0 and ins > 0:
                stack.insert(0, ins)
                continue
            if stack[0] > 0 and ins < 0:
                flg = 0
                while True:
                    if len(stack) == 0:
                        break
                    if stack[0] > 0 and ins > 0:
                        break
                    if stack[0] < 0 and ins < 0:
                        break
                    if stack[0] < 0 and ins > 0:
                        break
                    popv = stack.pop(0)
                    if abs(popv) == abs(ins):
                        flg = 1
                        break
                    if abs(popv) > abs(ins):
                        ins = popv
                if flg == 0:
                    stack.insert(0, ins)
            # print(stack)

        return stack[::-1]
