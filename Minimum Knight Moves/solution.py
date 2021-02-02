class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        q = [((0, 0), 0)]
        target = (x, y)
        if target == (0, 0):
            return 0
        visited = set()
        visited.add((0, 0))
        while q:
            s, step = q.pop(0)
            x = s[0]
            y = s[1]
            m1 = (x + 2, y - 1)
            m2 = (x + 2, y + 1)
            m3 = (x + 1, y + 2)
            m4 = (x - 1, y + 2)
            m5 = (x - 2, y - 1)
            m6 = (x - 2, y + 1)
            m7 = (x + 1, y - 2)
            m8 = (x - 1, y - 2)
            if m1 not in visited:
                if m1 == target:
                    return step + 1
                visited.add(m1)
                q.append((m1, step + 1))
            if m2 not in visited:
                if m2 == target:
                    return step + 1
                visited.add(m2)
                q.append((m2, step + 1))
            if m3 not in visited:
                if m3 == target:
                    return step + 1
                visited.add(m3)
                q.append((m3, step + 1))
            if m4 not in visited:
                if m4 == target:
                    return step + 1
                visited.add(m4)
                q.append((m4, step + 1))
            if m5 not in visited:
                if m5 == target:
                    return step + 1
                visited.add(m5)
                q.append((m5, step + 1))
            if m6 not in visited:
                if m6 == target:
                    return step + 1
                visited.add(m6)
                q.append((m6, step + 1))
            if m7 not in visited:
                if m7 == target:
                    return step + 1
                visited.add(m7)
                q.append((m7, step + 1))
            if m8 not in visited:
                if m8 == target:
                    return step + 1
                visited.add(m8)
                q.append((m8, step + 1))
