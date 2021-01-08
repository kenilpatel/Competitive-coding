import collections


class Solution(object):
    def getval(self):
        return False

    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        str = "0000"
        move_dict = {"0": ["1", "9"], "1": ["2", "0"], "2": ["1", "3"], "3": ["2", "4"], "4": [
            "5", "3"], "5": ["6", "4"], "6": ["7", "5"], "7": ["8", "6"], "8": ["7", "9"], "9": ["0", "8"]}
        target_dict = defaultdict(self.getval)
        for i in deadends:
            target_dict[i] = True
        g_depth = -1
        queue = [("0000", 0)]
        visited = defaultdict(self.getval)
        t = defaultdict(self.getval)
        t[target] = True
        visited["0000"] = True
        if target_dict["0000"] == True:
            return -1
        while len(queue) != 0:
            top, depth = queue[0]
            queue = queue[1:]
            if t[top]:
                return depth
            wheel1 = top[0]
            wheel2 = top[1]
            wheel3 = top[2]
            wheel4 = top[3]
            for m in move_dict[wheel1]:
                move = m + top[1:]
                if visited[move] == False and target_dict[move] == False:
                    if t[move]:
                        return depth + 1
                    visited[move] = True
                    queue.append((move, depth + 1))
            for m in move_dict[wheel2]:
                move = top[0] + m + top[2:]
                if visited[move] == False and target_dict[move] == False:
                    if t[move]:
                        return depth + 1
                    visited[move] = True
                    queue.append((move, depth + 1))
            for m in move_dict[wheel3]:
                move = top[0:2] + m + top[3:]
                if visited[move] == False and target_dict[move] == False:
                    if t[move]:
                        return depth + 1
                    visited[move] = True
                    queue.append((move, depth + 1))
            for m in move_dict[wheel4]:
                move = top[0:3] + m
                if visited[move] == False and target_dict[move] == False:
                    if t[move]:
                        return depth + 1
                    visited[move] = True
                    queue.append((move, depth + 1))
        return -1
